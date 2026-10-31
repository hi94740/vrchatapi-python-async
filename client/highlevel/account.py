"""Account snapshots, pipeline recovery and user presence independent of consumers."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Awaitable, Callable, Mapping
from typing import Any, TypeVar, cast

import vrchatapi
from vrchatapi.exceptions import UnauthorizedException
from vrchatapi.websocket import VRChatEvent, VRChatWebSocket, VRChatWebSocketError

from .api import VRChatAPI
from .presence import (
    VRCHAT_SPECIAL_LOCATION_STRINGS,
    parse_vrchat_location_string,
    process_vrchat_string,
)
from .types import CurrentUser, HighLevelUserData, User
from .world import WorldCache

_LOGGER = logging.getLogger(__name__)
_Result = TypeVar("_Result")


async def _gather(*awaitables):
    """Cancel sibling requests before allowing their client to be closed."""
    tasks = [asyncio.create_task(awaitable) for awaitable in awaitables]
    try:
        return await asyncio.gather(*tasks)
    except BaseException:
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        raise


class AccountIdMismatch(Exception):
    """Credentials resolved to a different account."""

    def __init__(self, expected: str, actual: str) -> None:
        self.expected = expected
        self.actual = actual
        super().__init__(f"Expected account {expected}, got {actual}")


class VRChatAccount:
    """Own a live account, exposing synchronous change notifications.

    Call start before using the snapshot and close on teardown. The account owns
    its API and, unless supplied explicitly, its world cache. Notifications run
    synchronously on the event loop and must not block. Supplying an awaitable
    before_user_remove hook enables queued membership changes and waits for
    cleanup before removing a user. An injected cache remains caller-owned.
    """

    def __init__(
        self,
        api: VRChatAPI,
        account_id: str,
        *,
        worlds: WorldCache | None = None,
        on_user: Callable[[VRChatUser, bool], None] | None = None,
        on_remove: Callable[[str], None] | None = None,
        before_user_remove: Callable[[str], Awaitable[None]] | None = None,
        on_event: Callable[
            [VRChatEvent | VRChatWebSocketError, HighLevelUserData | None], None
        ]
        | None = None,
        on_available: Callable[[bool], None] | None = None,
        on_auth_error: Callable[[Exception], None] | None = None,
        on_authenticated: Callable[[VRChatAPI], Awaitable[None]] | None = None,
        retry_delay: float = 60,
        inactive_timeout: float = 600,
    ) -> None:
        self.api = api
        self.account_id = account_id
        self.users: dict[str, VRChatUser] = {}
        self.current_user_data: CurrentUser
        self.worlds = (
            worlds
            if worlds is not None
            else WorldCache(self._get_world, retry_delay=retry_delay)
        )
        self._owns_worlds = worlds is None
        self.on_user = on_user
        self.on_remove = on_remove
        self.before_user_remove = before_user_remove
        self.on_event = on_event
        self.on_available = on_available
        self.on_auth_error = on_auth_error
        self.on_authenticated = on_authenticated
        self.retry_delay = retry_delay
        self.inactive_timeout = inactive_timeout
        self.available = False
        self.closed = False
        self._runner: asyncio.Task[None] | None = None
        self._receiver: asyncio.Task[None] | None = None
        self._pipeline_activity = asyncio.Event()
        self._tasks: set[asyncio.Task[Any]] = set()
        self._event_tasks: dict[str | None, asyncio.Task[None]] = {}
        self._mutation_tasks: dict[str, asyncio.Task[Any]] = {}
        self._active_mutations: dict[str, asyncio.Task[Any]] = {}
        self._removing: set[str] = set()
        self._user_versions: dict[str, int] = {}
        self._recovery_lock = asyncio.Lock()
        self.ws = None

    def _notify(self, callback, *args) -> None:
        if callback is not None:
            try:
                callback(*args)
            except Exception:
                _LOGGER.exception("Account subscriber failed")

    def _set_available(self, value: bool) -> None:
        if self.available != value:
            self.available = value
            self._notify(self.on_available, value)

    async def _get_world(self, world_id: str):
        return await self.api.get_world(world_id)

    def create_task(self, awaitable) -> asyncio.Task:
        task = asyncio.create_task(awaitable)
        self._tasks.add(task)
        task.add_done_callback(self._task_done)
        return task

    def _task_done(self, task: asyncio.Task) -> None:
        self._tasks.discard(task)
        if not task.cancelled() and (error := task.exception()) is not None:
            _LOGGER.error(
                "Account background task failed",
                exc_info=(type(error), error, error.__traceback__),
            )

    async def authenticate(self, initial: CurrentUser | None = None) -> None:
        data = initial if initial is not None else await self.api.get_current_user()
        if data["id"] != self.account_id:
            raise AccountIdMismatch(self.account_id, data["id"])
        self.current_user_data = data
        if self.on_authenticated is not None:
            await self.on_authenticated(self.api)

    async def start(self, initial: CurrentUser | None = None) -> None:
        try:
            await self.authenticate(initial)
            self.ws = await self._connect_ws(self.api)
            await self.fetch_users()
            self._set_available(True)
            self._receiver = asyncio.create_task(self._receive(self.ws))
            self._runner = asyncio.create_task(self._run())
        except BaseException:
            await self.close()
            raise

    async def _connect_ws(self, api: VRChatAPI) -> VRChatWebSocket:
        return await api.ws_connect(on_error=self._handle_ws_error)

    def _handle_ws_error(self, error: Exception) -> None:
        if isinstance(error, VRChatWebSocketError) and error.raw is not None:
            self._notify(self.on_event, error, None)

    async def _get_friends(self, offline: bool) -> list[User]:
        ids = self.current_user_data["offlineFriends" if offline else "onlineFriends"]
        pages = await _gather(
            *(
                self.api.get_friends(offset=offset, n=100, offline=offline)
                for offset in range(0, len(ids), 100)
            )
        )
        return [friend for page in pages for friend in page]

    async def fetch_users(self) -> None:
        versions = self._user_versions.copy()
        friend_ids = list(self.current_user_data["friends"])
        offline, online = await _gather(
            self._get_friends(True), self._get_friends(False)
        )
        if not self.transactional:
            friend_ids = self.current_user_data["friends"]
        for user_id in list(self.users):
            if user_id != self.account_id and user_id not in friend_ids:
                if self.transactional:

                    async def remove(user_id=user_id):
                        if self._user_versions.get(user_id, 0) == versions.get(
                            user_id, 0
                        ):
                            await self._remove_user(user_id)

                    await asyncio.shield(self._queue_user_operation(user_id, remove))
                else:
                    self.remove_user(user_id)
        await self.async_set_user(self.current_user_data)
        for data in (*offline, *online):
            await self._set_snapshot_user(data, versions.get(data["id"], 0))
        fetched = {data["id"] for data in (*offline, *online)}
        missing = await _gather(
            *(self.api.get_user(i) for i in friend_ids if i not in fetched)
        )
        for data in missing:
            await self._set_snapshot_user(data, versions.get(data["id"], 0))

    async def _set_snapshot_user(self, data: User, version: int) -> None:
        if not self.transactional:
            self.set_user(data)
            return

        async def apply() -> None:
            if self._user_versions.get(data["id"], 0) == version:
                self._set_user(data)

        await asyncio.shield(self._queue_user_operation(data["id"], apply))

    @property
    def transactional(self) -> bool:
        """Whether membership changes await consumer lifecycle cleanup."""
        return self.before_user_remove is not None

    def _require_sync_mode(self) -> None:
        if self.transactional:
            raise RuntimeError(
                "Use request_* or async_* user methods in transactional mode"
            )

    def _queue_user_operation(
        self, user_id: str, operation: Callable[[], Awaitable[_Result]]
    ) -> asyncio.Task[_Result]:
        if self.closed:
            raise RuntimeError("Account is closed")
        previous = self._mutation_tasks.get(user_id)
        if previous is not None and previous.done():
            previous = None

        async def run() -> _Result:
            # Even an eager task factory must leave the current notification stack.
            await asyncio.sleep(0)
            if previous is not None:
                await asyncio.shield(previous)
            if self.closed:
                raise RuntimeError("Account is closed")
            current = asyncio.current_task()
            assert current is not None
            self._active_mutations[user_id] = current
            try:
                return await operation()
            finally:
                self._active_mutations.pop(user_id, None)

        task = self.create_task(run())
        self._mutation_tasks[user_id] = task

        def done(completed: asyncio.Task[_Result]) -> None:
            if self._mutation_tasks.get(user_id) is completed:
                self._mutation_tasks.pop(user_id)

        task.add_done_callback(done)
        return task

    def _check_self_wait(self, user_id: str) -> None:
        if asyncio.current_task() is self._active_mutations.get(user_id):
            raise RuntimeError("A user operation cannot await its own queue")

    def set_user(self, data: User | CurrentUser, overwrite: bool = True) -> VRChatUser:
        self._require_sync_mode()
        return self._set_user(data, overwrite)

    def _set_user(self, data: User | CurrentUser, overwrite: bool = True) -> VRChatUser:
        if data["id"] in self._removing:
            raise RuntimeError("User removal has not completed")
        if (user := self.users.get(data["id"])) is None:
            user = VRChatUser(self, data["id"])
            self.users[user.id] = user
            self._user_versions[user.id] = self._user_versions.get(user.id, 0) + 1
            user.data = data
        elif overwrite:
            user.data = data
        return user

    def request_set_user(
        self, data: User | CurrentUser, overwrite: bool = True
    ) -> asyncio.Task[VRChatUser]:
        """Queue a user update without mutating data in the calling stack."""
        snapshot = data.copy()

        async def apply() -> VRChatUser:
            return self._set_user(snapshot, overwrite)

        return self._queue_user_operation(data["id"], apply)

    async def async_set_user(
        self, data: User | CurrentUser, overwrite: bool = True
    ) -> VRChatUser:
        """Wait for a queued update, or retain immediate legacy notifications."""
        if not self.transactional:
            return self.set_user(data, overwrite)
        self._check_self_wait(data["id"])
        return await asyncio.shield(self.request_set_user(data, overwrite))

    async def _ensure_user(self, user_id: str) -> VRChatUser:
        if (user := self.users.get(user_id)) is not None:
            return user
        return self._set_user(await self.api.get_user(user_id), overwrite=False)

    async def ensure_user(self, user_id: str) -> VRChatUser:
        if not self.transactional:
            return await self._ensure_user(user_id)
        self._check_self_wait(user_id)
        return await asyncio.shield(
            self._queue_user_operation(user_id, lambda: self._ensure_user(user_id))
        )

    def remove_user(self, user_id: str) -> None:
        self._require_sync_mode()
        if (user := self.users.pop(user_id, None)) is not None:
            user.close()
            self._notify(self.on_remove, user_id)

    async def _remove_user(self, user_id: str) -> None:
        if (user := self.users.get(user_id)) is None:
            return
        self._removing.add(user_id)
        # Fail closed: unsuccessful cleanup keeps the user pending removal.
        if self.before_user_remove is not None:
            await self.before_user_remove(user_id)
        user.close()
        self.users.pop(user_id)
        self._user_versions[user_id] = self._user_versions.get(user_id, 0) + 1
        self._removing.discard(user_id)
        self._notify(self.on_remove, user_id)

    def request_remove_user(self, user_id: str) -> asyncio.Task[None]:
        """Queue removal; the returned task completes after consumer cleanup."""
        return self._queue_user_operation(user_id, lambda: self._remove_user(user_id))

    async def async_remove_user(self, user_id: str) -> None:
        """Wait for removal without invalidating an active notification stack."""
        if not self.transactional:
            self.remove_user(user_id)
            return
        self._check_self_wait(user_id)
        await asyncio.shield(self.request_remove_user(user_id))

    async def handle_event(self, event: VRChatEvent) -> None:
        user_id = (
            event.content.get("userId") if isinstance(event.content, dict) else None
        )
        if self.transactional and user_id is not None:
            self._check_self_wait(user_id)
            await asyncio.shield(
                self._queue_user_operation(user_id, lambda: self._apply_event(event))
            )
            return
        await self._apply_event(event)

    async def _apply_event(self, event: VRChatEvent) -> None:
        content = event.content
        if not isinstance(content, dict):
            self._notify(self.on_event, event, None)
            return
        if isinstance(world := content.get("world"), dict) and (
            world_id := process_vrchat_string(world.get("id"))
        ):
            self.worlds.get(world_id, world)
        content = content.copy()
        world_id, _ = parse_vrchat_location_string(content.get("travelingToLocation"))
        if world_id and world_id not in VRCHAT_SPECIAL_LOCATION_STRINGS:
            content["travelingToWorldId"] = world_id
            self.create_task(self.worlds.get(world_id).get_data())
        user_id = content.get("userId")
        old_user = self.users.get(user_id) if user_id is not None else None
        self._notify(
            self.on_event,
            VRChatEvent(
                type=event.type,
                content=content,
                raw=event.raw,
                raw_content=event.raw_content,
            ),
            old_user.data.copy() if old_user is not None else None,
        )
        if user_id is None:
            return
        if event.type == "friend-delete":
            if self.transactional:
                await self._remove_user(user_id)
            else:
                self.remove_user(user_id)
            return
        user = await self._ensure_user(user_id)
        user.apply_event(event.type, content)

    def _dispatch_event(self, event: VRChatEvent) -> None:
        user_id = (
            event.content.get("userId") if isinstance(event.content, dict) else None
        )
        previous = self._event_tasks.get(user_id)
        task = self._event_tasks[user_id] = self.create_task(
            self._handle_pipeline_event(event, previous)
        )

        def event_done(done: asyncio.Task) -> None:
            if self._event_tasks.get(user_id) is done:
                self._event_tasks.pop(user_id)

        task.add_done_callback(event_done)

    async def _handle_pipeline_event(
        self, event: VRChatEvent, previous: asyncio.Task | None
    ) -> None:
        if previous is not None:
            await previous
        try:
            await self.handle_event(event)
        except Exception:
            _LOGGER.exception("Error applying pipeline event")

    async def _recover(self, failed_api: VRChatAPI) -> None:
        async with self._recovery_lock:
            if self.closed or self.api is not failed_api:
                return
            replacement = failed_api.copy()
            old_ws = self.ws
            self.api = replacement
            try:
                await self.authenticate()
                new_ws = await self._connect_ws(replacement)
                await self._stop_receiver()
                # Discard old pipeline work before applying the replacement snapshot.
                pending = list(self._event_tasks.values())
                for task in pending:
                    task.cancel()
                await asyncio.gather(*pending, return_exceptions=True)
                self._event_tasks.clear()
                await asyncio.gather(*tuple(self._mutation_tasks.values()))
                self.ws = new_ws
                self._receiver = asyncio.create_task(self._receive(new_ws))
                await self.fetch_users()
            except BaseException:
                if self.ws is not old_ws:
                    await self._stop_receiver()
                if self._receiver is None and not self.closed and old_ws is not None:
                    self._receiver = asyncio.create_task(self._receive(old_ws))
                self.api = failed_api
                self.ws = old_ws
                await replacement.close()
                raise
            await failed_api.close()
            self._set_available(True)

    async def _stop_receiver(self) -> None:
        receiver = self._receiver
        self._receiver = None
        if receiver is not None:
            receiver.cancel()
            await asyncio.gather(receiver, return_exceptions=True)

    async def _receive(self, ws: VRChatWebSocket) -> None:
        try:
            async for event in ws:
                self._dispatch_event(event)
                self._pipeline_activity.set()
        finally:
            self._pipeline_activity.set()

    async def _run(self) -> None:
        while not self.closed:
            failed_api = self.api
            timed_out = False
            try:
                # Application traffic, not heartbeat frames, refreshes this deadline.
                while not self.closed:
                    self._pipeline_activity.clear()
                    if self._receiver is not None and self._receiver.done():
                        self._receiver.result()
                        break
                    await asyncio.wait_for(
                        self._pipeline_activity.wait(), self.inactive_timeout
                    )
            except asyncio.CancelledError:
                raise
            except asyncio.TimeoutError:
                timed_out = True
            except Exception:
                _LOGGER.warning("Pipeline disconnected", exc_info=True)
            if self.closed:
                return
            if not timed_out:
                self._set_available(False)
            while not self.closed:
                try:
                    await self._recover(failed_api)
                except (UnauthorizedException, AccountIdMismatch) as exc:
                    self._notify(self.on_auth_error, exc)
                    return
                except Exception:
                    _LOGGER.warning("Account recovery failed; retrying", exc_info=True)
                    await asyncio.sleep(self.retry_delay)
                else:
                    break

    async def update_user(self, user_id: str, data: vrchatapi.UpdateUserRequest):
        failed_api = self.api
        try:
            return await failed_api.update_user(user_id, data)
        except UnauthorizedException:
            try:
                await self._recover(failed_api)
                return await self.api.update_user(user_id, data)
            except (UnauthorizedException, AccountIdMismatch) as exc:
                self._notify(self.on_auth_error, exc)
                raise

    async def close(self) -> None:
        if self.closed:
            return
        self.closed = True
        current_task = asyncio.current_task()
        tasks = [task for task in self._tasks if task is not current_task]
        if self._runner is not None:
            tasks.append(self._runner)
        if self._receiver is not None:
            tasks.append(self._receiver)
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        self._event_tasks.clear()
        self._mutation_tasks.clear()
        for user in self.users.values():
            user.close()
        if self._owns_worlds:
            await self.worlds.close()
        await self.api.close()
        self._set_available(False)


class VRChatUser:
    """Merged user snapshot and world subscriptions."""

    def __init__(self, account: VRChatAccount, user_id: str) -> None:
        self.account = account
        self.id = user_id
        self.world = None
        self._data: HighLevelUserData = {}
        self.closed = False

    @property
    def data(self) -> HighLevelUserData:
        return self._data

    @data.setter
    def data(self, value: Mapping[str, Any]) -> None:
        if self.account.transactional and (
            self.closed or self.account.users.get(self.id) is not self
        ):
            raise RuntimeError("User is no longer current")
        if self.account.transactional and (
            asyncio.current_task() is not self.account._active_mutations.get(self.id)
            or self.id in self.account._removing
        ):
            raise RuntimeError("Use queued account methods to update user data")
        value = cast(HighLevelUserData, dict(value))
        value["friend_of"] = self.account.account_id
        presence = value.get("presence") or {}
        world_id = process_vrchat_string(presence.get("world"))
        instance_id = process_vrchat_string(presence.get("instance"))
        location = (
            process_vrchat_string(value.get("location"))
            or process_vrchat_string(presence.get("location"))
            or world_id
            or instance_id
            or "offline"
        )
        value["location"] = location
        destination_id, _ = parse_vrchat_location_string(
            value.get("travelingToLocation")
        )
        value.pop("travelingToWorldId", None)
        if destination_id and destination_id not in VRCHAT_SPECIAL_LOCATION_STRINGS:
            value["travelingToWorldId"] = destination_id
        parsed_world, parsed_instance = parse_vrchat_location_string(location)
        value.setdefault("worldId", parsed_world or world_id)
        value.setdefault("instanceId", parsed_instance or instance_id)
        world_id = value["worldId"]
        if self._data.get("worldId") != world_id:
            if self.world is not None:
                self.world.unsubscribe(self._world_updated)
            self.world = None
            if world_id and world_id not in VRCHAT_SPECIAL_LOCATION_STRINGS:
                self.world = self.account.worlds.get(world_id)
                self.world.subscribe(self._world_updated)
                self.account.create_task(self.world.get_data())
        self._data = value
        self.account._notify(self.account.on_user, self, False)

    @property
    def destination_world(self):
        if world_id := self.data.get("travelingToWorldId"):
            return self.account.worlds.get(world_id)
        return None

    def _world_updated(self, _data) -> None:
        if self.account.transactional and (
            self.closed
            or self.account.closed
            or self.account.users.get(self.id) is not self
            or self.id in self.account._removing
        ):
            return
        self.account._notify(self.account.on_user, self, True)

    def apply_event(self, event_type: str, content: dict) -> None:
        if event_type == "friend-offline":
            self.data = {
                **self.data,
                "location": "offline",
                "worldId": "offline",
                "instanceId": "offline",
                "status": "offline",
                "statusDescription": "",
                "travelingToLocation": "",
            }
            return
        if (new_data := content.get("user")) is None:
            return
        if event_type == "user-update":
            self.data = {**self.data, **new_data}
            return
        new_data = new_data.copy()
        new_data.update(
            {
                key: value
                for key, value in content.items()
                if key not in {"user", "userId", "world"}
            }
        )
        explicit_location = "location" in new_data
        if not explicit_location:
            if event_type == "friend-active":
                new_data.update(
                    location="offline", worldId="offline", instanceId="offline"
                )
            else:
                new_data["location"] = self.data.get("location") or (
                    self.data.get("presence") or {}
                ).get("location")
        merged = {**self.data, **new_data}
        if explicit_location:
            merged.pop("worldId", None)
            merged.pop("instanceId", None)
            if "travelingToLocation" not in new_data:
                merged.pop("travelingToLocation", None)
        self.data = merged

    async def update_user(self, request: vrchatapi.UpdateUserRequest) -> None:
        if self.account.transactional and (
            self.closed or self.account.users.get(self.id) is not self
        ):
            raise RuntimeError("User is no longer current")
        if self.account.transactional:
            self.account._check_self_wait(self.id)
        new_data = await self.account.update_user(self.id, request)

        async def apply() -> None:
            if self.account.transactional and (
                self.closed or self.account.users.get(self.id) is not self
            ):
                return
            self._apply_user_update(new_data)

        if self.account.transactional:
            await asyncio.shield(self.account._queue_user_operation(self.id, apply))
        else:
            await apply()

    def _apply_user_update(self, new_data: User | CurrentUser) -> None:
        old_data = self.data.copy()
        presence = new_data.get("presence") or {}
        if process_vrchat_string(new_data.get("location")) is not None or any(
            process_vrchat_string(presence.get(key)) is not None
            for key in ("location", "world", "instance")
        ):
            for key in ("location", "worldId", "instanceId"):
                old_data.pop(key, None)
        self.data = {**old_data, **new_data}

    def close(self) -> None:
        self.closed = True
        if self.world is not None:
            self.world.unsubscribe(self._world_updated)
