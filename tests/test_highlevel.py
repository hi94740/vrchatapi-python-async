"""Library-owned account, presence and cache regression coverage."""

from __future__ import annotations

import asyncio
from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, Mock

import pytest
from test_async_sdk import MockVRCServer

from vrchatapi.exceptions import UnauthorizedException
from vrchatapi.highlevel import (
    AccountIdMismatch,
    VRChatAccount,
    VRChatAPI,
    VRChatUser,
    WorldCache,
)
from vrchatapi.highlevel.presence import is_user_in_game
from vrchatapi.websocket import VRChatEvent

CURRENT = {
    "id": "usr_self",
    "username": "self",
    "friends": ["usr_friend"],
    "onlineFriends": [],
    "offlineFriends": [],
}
FRIEND = {
    "id": "usr_friend",
    "location": "offline",
    "status": "active",
    "displayName": "Friend",
}


class Pipeline:
    def __init__(self) -> None:
        self.events: asyncio.Queue = asyncio.Queue()
        self.closed = False

    def __aiter__(self):
        return self

    async def __anext__(self):
        event = await self.events.get()
        if event is None:
            raise StopAsyncIteration
        return event

    async def close(self) -> None:
        self.closed = True
        self.events.put_nowait(None)


@pytest.fixture
async def account():
    pipeline = Pipeline()
    api = Mock(spec=VRChatAPI)
    api.get_current_user = AsyncMock(return_value=CURRENT.copy())
    api.get_user = AsyncMock(return_value=FRIEND.copy())
    api.get_friends = AsyncMock(return_value=[])
    api.get_world = AsyncMock(return_value={"id": "wrld_test", "name": "World"})
    api.ws_connect = AsyncMock(return_value=pipeline)
    api.close = AsyncMock(side_effect=pipeline.close)
    client = VRChatAccount(api, "usr_self", retry_delay=0.01)
    yield client
    await client.close()


@pytest.mark.parametrize(
    "body",
    [
        pytest.param(
            {
                "id": "usr_self",
                "unknownField": {"nested": 42},
                "statusDescription": None,
            },
            id="unknown-and-null",
        ),
        pytest.param({"statusDescription": ""}, id="partial-and-empty"),
    ],
)
async def test_raw_dictionary_contract(body: dict) -> None:
    server = MockVRCServer()
    server.body = body
    await server.start()
    try:
        async with VRChatAPI() as api:
            api.api_client.configuration.host = server.base_url
            result = await api.get_current_user()
            assert result == body
    finally:
        await server.stop()


async def test_dictionary_client_retains_auth_errors() -> None:
    server = MockVRCServer()
    server.raw_body = '{"abcdefghijklmnopqrstu":["emailOtp"]}'
    await server.start()
    try:
        async with VRChatAPI() as api:
            api.api_client.configuration.host = server.base_url
            with pytest.raises(UnauthorizedException, match="Email 2 Factor"):
                await api.get_current_user()
    finally:
        await server.stop()


async def test_cookie_copy_user_agent_and_close() -> None:
    async with VRChatAPI(
        {"username": "user", "password": "pass"},
        {"auth": "token", "twoFactorAuth": ""},
        user_agent="Test/1",
    ) as api:
        async with api.copy() as copied:
            assert copied.cookie == {"auth": "token"}
            assert copied.config == api.config
            assert copied.api_client.user_agent == "Test/1"
            copied.clear_cookie()
            assert copied.cookie == {}
            assert api.cookie == {"auth": "token"}
    await api.close()


async def test_start_snapshot_and_notifications(account: VRChatAccount) -> None:
    account.on_user = Mock()
    account.on_authenticated = AsyncMock()
    await account.start()
    assert account.available
    assert set(account.users) == {"usr_self", "usr_friend"}
    account.on_authenticated.assert_awaited_once_with(account.api)
    account.api.get_user.assert_awaited_once_with("usr_friend")
    assert account.on_user.call_count == 2


async def test_setup_failure_closes_client(account: VRChatAccount) -> None:
    account.api.get_current_user.return_value = {"id": "wrong"}
    with pytest.raises(AccountIdMismatch):
        await account.start()
    account.api.close.assert_awaited_once()
    assert account.closed


async def test_pagination_and_missing_friends(account: VRChatAccount) -> None:
    account.current_user_data = {
        **CURRENT,
        "onlineFriends": [str(i) for i in range(101)],
    }
    account.api.get_friends.side_effect = [[FRIEND], []]
    await account.fetch_users()
    assert [
        call.kwargs["offset"] for call in account.api.get_friends.await_args_list
    ] == [0, 100]
    account.api.get_user.assert_not_awaited()


async def test_pagination_error_propagates(account: VRChatAccount) -> None:
    account.current_user_data = {**CURRENT, "onlineFriends": ["usr_friend"]}
    account.api.get_friends.side_effect = RuntimeError("failed")
    with pytest.raises(RuntimeError, match="failed"):
        await account.fetch_users()


async def test_new_user_preserves_outer_location(account: VRChatAccount) -> None:
    await account.handle_event(
        VRChatEvent(
            "friend-online",
            {
                "userId": "usr_friend",
                "user": {"id": "usr_friend", "status": "active"},
                "location": "wrld_test:instance",
            },
        )
    )
    user = account.users["usr_friend"]
    assert user.data["location"] == "wrld_test:instance"
    assert user.data["worldId"] == "wrld_test"
    assert is_user_in_game(user.data)


async def test_ensure_does_not_overwrite_concurrent_insert(
    account: VRChatAccount,
) -> None:
    started = asyncio.Event()
    release = asyncio.Event()

    async def fetch(user_id: str) -> dict:
        started.set()
        await release.wait()
        return FRIEND.copy()

    account.api.get_user.side_effect = fetch
    task = asyncio.create_task(account.ensure_user("usr_friend"))
    await started.wait()
    newer = account.set_user({**FRIEND, "statusDescription": "new"})
    release.set()
    assert await task is newer
    assert newer.data["statusDescription"] == "new"


@pytest.mark.parametrize(
    ("response", "location"),
    [
        pytest.param({"statusDescription": ""}, "wrld_test:instance", id="partial"),
        pytest.param({"location": "offline"}, "offline", id="location"),
        pytest.param({"presence": {"world": "private"}}, "private", id="presence"),
    ],
)
async def test_partial_update(
    account: VRChatAccount, response: dict, location: str
) -> None:
    user = account.set_user({**FRIEND, "location": "wrld_test:instance"})
    account.api.update_user = AsyncMock(return_value=response)
    await user.update_user(Mock())
    assert user.data["location"] == location
    assert user.data["status"] == "active"


async def test_active_offline_delete_and_unknown_events(account: VRChatAccount) -> None:
    account.on_remove = Mock()
    await account.handle_event(VRChatEvent("see-notification", "notification-id"))
    await account.handle_event(VRChatEvent("friend-delete", {"userId": "missing"}))
    account.api.get_user.assert_not_awaited()
    await account.handle_event(
        VRChatEvent("friend-active", {"userId": "usr_friend", "user": FRIEND.copy()})
    )
    assert not is_user_in_game(account.users["usr_friend"].data)
    assert account.users["usr_friend"].data["status"] == "active"
    await account.handle_event(VRChatEvent("friend-offline", {"userId": "usr_friend"}))
    assert account.users["usr_friend"].data["statusDescription"] == ""
    await account.handle_event(VRChatEvent("friend-delete", {"userId": "usr_friend"}))
    assert not account.users
    account.on_remove.assert_called_once_with("usr_friend")


async def test_embedded_world_and_destination(account: VRChatAccount) -> None:
    await account.handle_event(
        VRChatEvent(
            "friend-location",
            {
                "userId": "usr_friend",
                "user": FRIEND,
                "location": "wrld_test:instance",
                "world": {"id": "wrld_test", "name": "World"},
                "travelingToLocation": "wrld_next:instance",
            },
        )
    )
    user = account.users["usr_friend"]
    assert user.world.data["name"] == "World"
    assert user.destination_world.id == "wrld_next"


@pytest.mark.parametrize(
    "destination",
    [
        pytest.param({}, id="omitted"),
        pytest.param({"travelingToLocation": ""}, id="empty"),
        pytest.param({"travelingToLocation": "private"}, id="private"),
    ],
)
async def test_private_location_clears_previous_destination(
    account: VRChatAccount, destination: dict
) -> None:
    await account.handle_event(
        VRChatEvent(
            "friend-location",
            {
                "userId": "usr_friend",
                "user": FRIEND.copy(),
                "location": "traveling",
                "travelingToLocation": "wrld_test:instance",
            },
        )
    )
    user = account.users["usr_friend"]
    assert user.destination_world.id == "wrld_test"
    await account.handle_event(
        VRChatEvent(
            "friend-location",
            {
                "userId": "usr_friend",
                "user": {"id": "usr_friend"},
                "location": "wrld_test:instance",
                **destination,
            },
        )
    )
    assert user.destination_world is None
    await account.handle_event(
        VRChatEvent(
            "friend-location",
            {
                "userId": "usr_friend",
                "user": {"id": "usr_friend"},
                "location": "private",
                **destination,
            },
        )
    )
    assert user.data["location"] == "private"
    assert user.data["worldId"] == "private"
    assert user.world is None
    assert user.destination_world is None
    assert "travelingToWorldId" not in user.data
    assert user.data["status"] == "active"


async def test_world_fetch_shared_and_cancellation_isolated() -> None:
    fetch = AsyncMock(return_value={"id": "wrld_test", "name": "World"})
    cache = WorldCache(fetch)
    assert cache.sorted_names == ()
    world = cache.get("wrld_test")
    first = asyncio.create_task(world.get_data())
    second = asyncio.create_task(world.get_data())
    await asyncio.sleep(0)
    first.cancel()
    with pytest.raises(asyncio.CancelledError):
        await first
    assert (await second)["name"] == "World"
    assert cache.sorted_names == ("World",)
    fetch.assert_awaited_once()
    await cache.close()


async def test_world_names_cache_updates_and_reuses_snapshot() -> None:
    fetch = AsyncMock()
    cache = WorldCache(fetch)
    assert cache.sorted_names == ()
    first = cache.get("wrld_first", {"name": "B"})
    cache.get("wrld_second", {"name": "A"})
    cache.get("wrld_duplicate", {"name": "B"})
    cache.get("wrld_unknown")
    assert cache.sorted_names == ("A", "B")
    names = cache.sorted_names
    assert cache.sorted_names is names

    cache.get("wrld_first", {"name": "B", "description": "Updated"})
    assert cache.sorted_names is names
    observed = []
    first.subscribe(lambda _: observed.append(cache.sorted_names))
    first.data = {"name": "C"}
    assert observed == [("A", "B", "C")]
    assert cache.sorted_names == ("A", "B", "C")
    first.data = None
    assert cache.sorted_names == ("A", "B")
    first.data = {"name": "D"}
    assert cache.sorted_names == ("A", "B", "D")
    other = WorldCache(AsyncMock())
    assert other.sorted_names == ()
    fetch.assert_not_awaited()
    await cache.close()
    assert cache.sorted_names == ()
    await other.close()


async def test_world_names_cache_prunes_duplicate_names() -> None:
    cache = WorldCache(AsyncMock())
    first = cache.get("wrld_first", {"name": "Shared"})
    second = cache.get("wrld_second", {"name": "Shared"})
    assert cache.sorted_names == ("Shared",)

    first.last_updated = datetime.now(timezone.utc) - timedelta(days=2)
    cache.last_pruned = datetime.min.replace(tzinfo=timezone.utc)
    cache.get("wrld_unknown")
    assert "wrld_first" not in cache.registry
    assert cache.sorted_names == ("Shared",)

    second.last_updated = datetime.now(timezone.utc) - timedelta(days=2)
    cache.last_pruned = datetime.min.replace(tzinfo=timezone.utc)
    cache.get("wrld_unknown")
    assert cache.sorted_names == ()
    await cache.close()


async def test_world_push_pruning_and_owned_shutdown() -> None:
    fetch = AsyncMock(side_effect=RuntimeError("failed"))
    cache = WorldCache(fetch, retry_delay=0.001)
    world = cache.get("wrld_test")
    callback = Mock()
    unsubscribe = world.subscribe(callback)
    world.data = {"id": "wrld_test", "name": "Pushed"}
    assert await world.get_data() == world.data
    fetch.assert_not_awaited()
    unsubscribe()
    unsubscribe()
    world.last_updated = datetime.now(timezone.utc) - timedelta(days=2)
    cache.last_pruned = datetime.min.replace(tzinfo=timezone.utc)
    cache.get("wrld_other")
    assert "wrld_test" not in cache.registry
    waiting = asyncio.create_task(cache.get("wrld_other").get_data())
    await asyncio.sleep(0)
    await cache.close()
    with pytest.raises(asyncio.CancelledError):
        await waiting


async def test_recovery_replaces_and_closes_connection(account: VRChatAccount) -> None:
    await account.start()
    old = account.api
    operations = []
    replacement = Mock(spec=VRChatAPI)
    replacement.get_current_user = AsyncMock(return_value=CURRENT)
    replacement.get_user = AsyncMock(return_value=FRIEND)
    replacement.get_friends = AsyncMock(return_value=[])
    replacement.ws_connect = AsyncMock(
        side_effect=lambda: operations.append("connect") or Pipeline()
    )
    replacement.close = AsyncMock()
    old.copy.return_value = replacement
    old.close.side_effect = lambda: operations.append("close")
    await account._recover(old)
    await asyncio.sleep(0)
    assert account.api is replacement
    assert operations == ["connect", "close"]
    old.close.assert_awaited_once()
    assert account.available
    await account.close()
    replacement.close.assert_awaited_once()


async def test_timeout_recovery_keeps_account_available(
    account: VRChatAccount,
) -> None:
    await account.start()
    availability = []
    account.on_available = availability.append
    old = account.api
    operations = []
    old_closed = asyncio.Event()

    async def close_old() -> None:
        operations.append("close")
        old_closed.set()

    replacement = Mock(spec=VRChatAPI)
    replacement.get_current_user = AsyncMock(return_value=CURRENT)
    replacement.get_user = AsyncMock(return_value=FRIEND)
    replacement.get_friends = AsyncMock(return_value=[])
    replacement.ws_connect = AsyncMock(
        side_effect=lambda: operations.append("connect") or Pipeline()
    )
    replacement.close = AsyncMock()
    old.copy.return_value = replacement
    old.close.side_effect = close_old
    account.inactive_timeout = 0.001

    await asyncio.wait_for(old_closed.wait(), 1)

    assert operations == ["connect", "close"]
    assert availability == []
    assert account.available
    await account.close()


async def test_failed_recovery_closes_replacement(account: VRChatAccount) -> None:
    old = account.api
    replacement = Mock(spec=VRChatAPI)
    replacement.get_current_user = AsyncMock(side_effect=UnauthorizedException())
    replacement.close = AsyncMock()
    old.copy.return_value = replacement
    with pytest.raises(UnauthorizedException):
        await account._recover(old)
    assert account.api is old
    replacement.close.assert_awaited_once()


@pytest.mark.parametrize("stage", ["get_current_user", "ws_connect"])
async def test_timeout_keeps_processing_old_pipeline_until_replacement(
    account: VRChatAccount, stage: str
) -> None:
    account.inactive_timeout = 0.01
    await account.start()
    old_api = account.api
    old_ws = account.ws
    old_receiver = account._receiver
    new_ws = Pipeline()
    started = asyncio.Event()
    proceed = asyncio.Event()
    recovered = asyncio.Event()
    availability: list[bool] = []
    account.on_available = availability.append
    changed = asyncio.Event()
    account.on_user = lambda user, world: changed.set()
    replacement = Mock(
        get_current_user=AsyncMock(return_value=CURRENT.copy()),
        get_friends=AsyncMock(return_value=[]),
        get_user=AsyncMock(return_value=FRIEND.copy()),
        ws_connect=AsyncMock(return_value=new_ws),
        close=AsyncMock(side_effect=new_ws.close),
    )
    result = getattr(replacement, stage).return_value

    async def wait_for_replacement() -> object:
        started.set()
        await proceed.wait()
        return result

    async def close_old() -> None:
        await old_ws.close()
        recovered.set()

    getattr(replacement, stage).side_effect = wait_for_replacement
    old_api.copy.return_value = replacement
    old_api.close.side_effect = close_old
    await asyncio.wait_for(started.wait(), 1)
    old_ws.events.put_nowait(
        VRChatEvent(
            "user-update",
            {"userId": "usr_friend", "user": {"statusDescription": "during recovery"}},
        )
    )
    await asyncio.wait_for(changed.wait(), 1)
    assert account.users["usr_friend"].data["statusDescription"] == "during recovery"
    assert not old_ws.closed
    assert availability == []
    account.inactive_timeout = 600
    proceed.set()
    await asyncio.wait_for(recovered.wait(), 1)
    assert old_receiver.done()
    assert old_ws.closed
    assert account.ws is new_ws
    changed.clear()
    new_ws.events.put_nowait(
        VRChatEvent(
            "user-update",
            {"userId": "usr_friend", "user": {"statusDescription": "replacement"}},
        )
    )
    await asyncio.wait_for(changed.wait(), 1)
    assert account.users["usr_friend"].data["statusDescription"] == "replacement"
    assert availability == []
    receiver = account._receiver
    await account.close()
    assert receiver.done()
    assert new_ws.closed


async def test_replacement_receives_events_during_snapshot(
    account: VRChatAccount,
) -> None:
    await account.start()
    old_api = account.api
    new_ws = Pipeline()
    fetching = asyncio.Event()
    proceed = asyncio.Event()
    changed = asyncio.Event()
    account.on_user = lambda user, world: changed.set()

    async def fetch_user(user_id: str) -> dict:
        fetching.set()
        await proceed.wait()
        return FRIEND.copy()

    old_api.copy.return_value = Mock(
        get_current_user=AsyncMock(return_value=CURRENT.copy()),
        get_friends=AsyncMock(return_value=[]),
        get_user=AsyncMock(side_effect=fetch_user),
        ws_connect=AsyncMock(return_value=new_ws),
        close=AsyncMock(side_effect=new_ws.close),
    )
    recovery = account.create_task(account._recover(old_api))
    await asyncio.wait_for(fetching.wait(), 1)
    changed.clear()
    new_ws.events.put_nowait(
        VRChatEvent(
            "user-update",
            {"userId": "usr_friend", "user": {"statusDescription": "during snapshot"}},
        )
    )
    await asyncio.wait_for(changed.wait(), 1)
    assert account.users["usr_friend"].data["statusDescription"] == "during snapshot"
    proceed.set()
    await asyncio.wait_for(recovery, 1)


async def test_failed_snapshot_resumes_old_pipeline(account: VRChatAccount) -> None:
    await account.start()
    old_api = account.api
    old_ws = account.ws
    new_ws = Pipeline()
    replacement = Mock(
        get_current_user=AsyncMock(return_value=CURRENT.copy()),
        get_friends=AsyncMock(return_value=[]),
        get_user=AsyncMock(side_effect=RuntimeError("snapshot failed")),
        ws_connect=AsyncMock(return_value=new_ws),
        close=AsyncMock(side_effect=new_ws.close),
    )
    old_api.copy.return_value = replacement
    with pytest.raises(RuntimeError, match="snapshot failed"):
        await account._recover(old_api)
    assert account.ws is old_ws
    assert account.api is old_api
    assert new_ws.closed
    assert not old_ws.closed
    changed = asyncio.Event()
    account.on_user = lambda user, world: changed.set()
    old_ws.events.put_nowait(
        VRChatEvent(
            "user-update",
            {"userId": "usr_friend", "user": {"statusDescription": "after failure"}},
        )
    )
    await asyncio.wait_for(changed.wait(), 1)
    assert account.users["usr_friend"].data["statusDescription"] == "after failure"
    assert account.available


async def test_close_during_timeout_recovery_stops_receiver(
    account: VRChatAccount,
) -> None:
    account.inactive_timeout = 0.01
    await account.start()
    old_ws = account.ws
    receiver = account._receiver
    started = asyncio.Event()

    async def authenticate() -> dict:
        started.set()
        await asyncio.Event().wait()
        return CURRENT.copy()

    replacement = Mock(
        get_current_user=AsyncMock(side_effect=authenticate), close=AsyncMock()
    )
    account.api.copy.return_value = replacement
    await asyncio.wait_for(started.wait(), 1)
    await asyncio.wait_for(account.close(), 1)
    assert receiver.done()
    assert account._runner.done()
    assert old_ws.closed
    assert not account.available
    replacement.close.assert_awaited_once()


async def test_external_cache_is_not_closed(account: VRChatAccount) -> None:
    cache = WorldCache(AsyncMock())
    other = VRChatAccount(Mock(close=AsyncMock()), "other", worlds=cache)
    await other.close()
    assert not cache.closed
    await cache.close()


async def test_pipeline_events_processed_in_order(account: VRChatAccount) -> None:
    await account.start()
    changed = asyncio.Event()
    account.on_user = lambda user, world: changed.set()
    await account.ws.events.put(
        VRChatEvent(
            "user-update",
            {"userId": "usr_friend", "user": {"statusDescription": "new"}},
        )
    )
    await asyncio.wait_for(changed.wait(), 1)
    assert account.users["usr_friend"].data["statusDescription"] == "new"
    assert account.users["usr_friend"].data["displayName"] == "Friend"


async def test_disconnect_auth_failure_notifies_and_stops(
    account: VRChatAccount,
) -> None:
    notified = asyncio.Event()
    account.on_auth_error = lambda error: notified.set()
    await account.start()
    account.api.copy.return_value = Mock(
        get_current_user=AsyncMock(side_effect=UnauthorizedException()),
        close=AsyncMock(),
    )
    await account.ws.close()
    await asyncio.wait_for(notified.wait(), 1)
    assert not account.available
    await account._runner


async def test_world_retry_and_push_during_wait() -> None:
    fetched = asyncio.Event()
    attempts = 0

    async def fetch(world_id: str) -> dict:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise RuntimeError("temporary failure")
        fetched.set()
        return {"id": world_id, "name": "Retried"}

    cache = WorldCache(fetch, retry_delay=0.001)
    try:
        world = cache.get("wrld_test")
        assert (await world.get_data())["name"] == "Retried"
        assert fetched.is_set()
        assert attempts == 2
    finally:
        await cache.close()


async def test_world_subscription_snapshot() -> None:
    cache = WorldCache(AsyncMock())
    world = cache.get("wrld_test")
    second = Mock()
    world.subscribe(lambda data: world.unsubscribe(second))
    world.subscribe(second)
    world.data = {"name": "World"}
    second.assert_called_once_with(world.data)
    await cache.close()


async def test_default_caches_are_account_scoped(account: VRChatAccount) -> None:
    other = VRChatAccount(Mock(close=AsyncMock()), "other")
    try:
        assert account.worlds.fetch.__self__ is account
        account.worlds.get("wrld_test", {"name": "World"})
        assert not other.worlds.registry
    finally:
        await other.close()


async def test_pagination_cancels_siblings_on_error(account: VRChatAccount) -> None:
    account.current_user_data = {
        **CURRENT,
        "onlineFriends": [str(i) for i in range(101)],
    }
    started = asyncio.Event()
    cancelled = asyncio.Event()

    async def page(offset: int, n: int, offline: bool) -> list:
        if offset == 0:
            await started.wait()
            raise RuntimeError("page failed")
        started.set()
        try:
            await asyncio.Event().wait()
        finally:
            cancelled.set()

    account.api.get_friends.side_effect = page
    with pytest.raises(RuntimeError, match="page failed"):
        await account.fetch_users()
    assert cancelled.is_set()


async def test_reauthentication_retries_user_update(account: VRChatAccount) -> None:
    old = account.api
    old.update_user = AsyncMock(side_effect=UnauthorizedException())
    replacement = Mock(spec=VRChatAPI)
    replacement.get_current_user = AsyncMock(return_value=CURRENT)
    replacement.get_user = AsyncMock(return_value=FRIEND)
    replacement.get_friends = AsyncMock(return_value=[])
    replacement.ws_connect = AsyncMock(return_value=Pipeline())
    replacement.close = AsyncMock()
    replacement.update_user = AsyncMock(return_value={"statusDescription": "updated"})
    old.copy.return_value = replacement
    assert await account.update_user("usr_friend", Mock()) == {
        "statusDescription": "updated"
    }
    replacement.update_user.assert_awaited_once()
    old.close.assert_awaited_once()


@pytest.mark.parametrize(
    "content",
    [
        pytest.param({"user": {"location": "wrld_test:instance"}}, id="nested"),
        pytest.param(
            {"user": {"location": "offline"}, "location": "wrld_test:instance"},
            id="outer-wins",
        ),
    ],
)
async def test_event_location_replaces_derived_ids(
    account: VRChatAccount, content: dict
) -> None:
    user = account.set_user(FRIEND.copy())
    account.worlds.get("wrld_test", {"id": "wrld_test", "name": "World"})
    await account.handle_event(
        VRChatEvent("friend-online", {"userId": "usr_friend", **content})
    )
    assert user.data["location"] == "wrld_test:instance"
    assert user.data["worldId"] == "wrld_test"
    assert user.data["instanceId"] == "instance"
    assert user.world.data["name"] == "World"
    assert user.data["displayName"] == "Friend"


async def test_pipeline_slow_user_does_not_block_other_users(
    account: VRChatAccount,
) -> None:
    await account.start()
    started = asyncio.Event()
    release = asyncio.Event()
    known_updated = asyncio.Event()
    removed = asyncio.Event()

    async def fetch(user_id: str) -> dict:
        started.set()
        await release.wait()
        return {"id": user_id, "status": "active"}

    def updated(user: VRChatUser, world: bool) -> None:
        if user.id == "usr_friend" and user.data["status"] == "offline":
            known_updated.set()

    account.api.get_user.reset_mock()
    account.api.get_user.side_effect = fetch
    account.on_user = updated
    account.on_remove = lambda user_id: removed.set()
    account.ws.events.put_nowait(
        VRChatEvent(
            "friend-online", {"userId": "usr_new", "user": {"status": "active"}}
        )
    )
    await asyncio.wait_for(started.wait(), 1)
    account.ws.events.put_nowait(VRChatEvent("friend-delete", {"userId": "usr_new"}))
    account.ws.events.put_nowait(
        VRChatEvent("friend-offline", {"userId": "usr_friend"})
    )
    await asyncio.wait_for(known_updated.wait(), 1)
    assert not removed.is_set()
    release.set()
    await asyncio.wait_for(removed.wait(), 1)
    assert "usr_new" not in account.users
    account.api.get_user.assert_awaited_once_with("usr_new")


@pytest.mark.parametrize("operation", ["close", "recover"])
async def test_pending_pipeline_fetch_cancelled_before_teardown(
    account: VRChatAccount, operation: str
) -> None:
    await account.start()
    started = asyncio.Event()
    cancelled = asyncio.Event()

    async def fetch(user_id: str) -> dict:
        started.set()
        try:
            await asyncio.Event().wait()
        finally:
            cancelled.set()

    async def close_api() -> None:
        assert cancelled.is_set()

    account.api.get_user.side_effect = fetch
    account.api.close.side_effect = close_api
    account.ws.events.put_nowait(
        VRChatEvent(
            "friend-online", {"userId": "usr_new", "user": {"status": "active"}}
        )
    )
    await asyncio.wait_for(started.wait(), 1)
    replacement = Mock(
        get_current_user=AsyncMock(return_value=CURRENT.copy()),
        get_friends=AsyncMock(return_value=[]),
        get_user=AsyncMock(return_value=FRIEND.copy()),
        ws_connect=AsyncMock(return_value=Pipeline()),
        close=AsyncMock(),
    )
    account.api.copy.return_value = replacement
    operations = {
        "close": account.close,
        "recover": lambda: account._recover(account.api),
    }
    await asyncio.wait_for(operations[operation](), 1)
    assert cancelled.is_set()
    assert "usr_new" not in account.users
