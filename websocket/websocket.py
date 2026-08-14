"""VRChat Websocket (Pipeline) API client.

The VRChat Websocket API, also known as "the pipeline", pushes real-time
updates to the authenticated client (invites, friend requests, friend online
events, group updates, ...). The connection is receive-only: the client only
listens for messages.

The connection URL is ``wss://pipeline.vrchat.cloud/?authToken=<auth cookie>``
where ``authToken`` is the ``auth`` cookie obtained by logging in through the
REST API. A proper ``User-Agent`` header is also required.

Most messages are double-encoded: the outer envelope is JSON of the form
``{"type": "...", "content": "..."}`` and the ``content`` field is itself a
stringified JSON object. This client automatically unpacks ``content`` into a
plain ``dict`` (see :class:`VRChatEvent`). The ``see-notification`` and
``hide-notification`` events carry a plain notification-ID string instead, and
``clear-notification`` has no content at all.

Example::

    import asyncio

    import vrchatapi
    from vrchatapi.api import authentication_api
    from vrchatapi.websocket import VRChatWebSocket


    async def main():
        configuration = vrchatapi.Configuration(username="user", password="pass")
        async with vrchatapi.ApiClient(configuration) as api_client:
            await authentication_api.AuthenticationApi(api_client).get_current_user()
            ws = VRChatWebSocket.from_client(api_client)

            @ws.on("friend-online")
            async def on_friend_online(event):
                print("friend online:", event.content["user"]["displayName"])

            await ws.run()


    if __name__ == "__main__":
        asyncio.run(main())
"""

import asyncio
import inspect
import json
import logging
import uuid
from typing import Any, Callable, Dict, FrozenSet, List, Optional
from urllib.parse import quote

import aiohttp

__all__ = [
    "VRChatWebSocket",
    "VRChatEvent",
    "VRChatWebSocketError",
    "get_auth_cookie",
    "DEFAULT_ENDPOINT",
    "DEFAULT_USER_AGENT",
    "DEFAULT_HEARTBEAT_INTERVAL",
    "WS_EVENT_TYPES",
]

logger = logging.getLogger(__name__)

DEFAULT_ENDPOINT = "wss://pipeline.vrchat.cloud"
DEFAULT_USER_AGENT = "vrchatapi-py"
DEFAULT_HEARTBEAT_INTERVAL = 30.0

#: End of stream sentinel pushed onto the shared queue to stop ``async for``.
_END = object()

#: Events whose ``content`` is a plain notification-ID string, not JSON.
_STRING_CONTENT_EVENTS: FrozenSet[str] = frozenset(
    {"see-notification", "hide-notification"}
)

#: Events that carry no ``content`` at all.
_NO_CONTENT_EVENTS: FrozenSet[str] = frozenset({"clear-notification"})

#: All event types documented at https://vrchat.community/websocket.
WS_EVENT_TYPES: FrozenSet[str] = frozenset(
    {
        # Notification events
        "notification",
        "response-notification",
        "see-notification",
        "hide-notification",
        "clear-notification",
        "notification-v2",
        "notification-v2-update",
        "notification-v2-delete",
        # Friend events
        "friend-add",
        "friend-delete",
        "friend-online",
        "friend-active",
        "friend-offline",
        "friend-update",
        "friend-location",
        # User events
        "user-update",
        "user-location",
        "user-badge-assigned",
        "user-badge-unassigned",
        "content-refresh",
        "economy-update",
        "modified-image-update",
        "instance-queue-joined",
        "instance-queue-ready",
        # Group events
        "group-joined",
        "group-left",
        "group-member-updated",
        "group-role-updated",
    }
)


class VRChatWebSocketError(Exception):
    """Raised for pipeline-level errors (server ``{"err": ...}`` messages)."""

    def __init__(self, message: str, *, raw: Optional[str] = None) -> None:
        super().__init__(message)
        self.message = message
        self.raw = raw


class VRChatEvent:
    """A single decoded message received from the pipeline.

    Attributes:
        type: The event type, e.g. ``"friend-online"``.
        content: The decoded ``content`` field. Usually a ``dict`` (the
            double-encoded JSON payload); a plain ``str`` for
            ``see-notification`` / ``hide-notification``; ``None`` for
            ``clear-notification``.
        raw: The complete raw JSON message as received over the wire.
        raw_content: The raw ``content`` field before decoding (``None`` when
            the event carries no content).
    """

    __slots__ = ("type", "content", "raw", "raw_content")

    def __init__(
        self,
        type: str,
        content: Any = None,
        raw: str = "",
        raw_content: Optional[str] = None,
    ) -> None:
        self.type = type
        self.content = content
        self.raw = raw
        self.raw_content = raw_content

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return (
            f"VRChatEvent(type={self.type!r}, content={self.content!r}, "
            f"raw={self.raw!r}, raw_content={self.raw_content!r})"
        )


def get_auth_cookie(api_client) -> Optional[str]:
    """Return the ``auth`` cookie value stored on an ``ApiClient``.

    The cookie is populated by the login flow (``GET /auth/user``). Returns
    ``None`` when the client has not logged in yet.
    """
    rest_client = getattr(api_client, "rest_client", None)
    cookie_jar = getattr(rest_client, "cookie_jar", None)
    if cookie_jar is None:
        return None
    for cookie in cookie_jar:
        if cookie.name == "auth":
            return cookie.value
    return None


class VRChatWebSocket:
    """Async client for the VRChat Websocket (Pipeline) API.

    Events can be consumed two ways, at the same time:

    * callbacks registered with :meth:`on` / :meth:`on_event`
      (``async def`` handlers that receive a :class:`VRChatEvent`), and
    * by iterating::

          async for event in ws:
              ...

      The iterator yields every event that the connection delivers and stops
      when the client is closed.

    Usage::

        ws = VRChatWebSocket(auth_token="authcookie_...", user_agent="MyApp/1.0 me@example.com")

        @ws.on("friend-online")
        async def on_friend_online(event):
            print("online:", event.content["user"]["displayName"])

        await ws.run()          # blocks, reconnects automatically
        # or, without auto-reconnect:
        # ws = VRChatWebSocket(..., auto_reconnect=False)
        # await ws.run()

    Args:
        auth_token: The ``auth`` cookie value obtained by logging in.
        user_agent: User-Agent header; the pipeline rejects connections
            without a proper one.
        endpoint: Websocket base URL.
        auto_reconnect: When ``True`` (default), :meth:`run` reconnects with
            exponential backoff after the connection drops or the server
            reports an error. When ``False``, :meth:`run` returns once the
            connection is closed.
        reconnect_max_delay: Upper bound (seconds) for the exponential
            reconnect backoff (1s, 2s, 4s, ... capped at this value).
        heartbeat_interval: Interval (seconds) for the application-level
            heartbeat message that keeps the connection alive; ``None``
            disables it. The server is receive-only per the documentation,
            but the official clients (and the website) send heartbeats.
        session: Optional pre-existing ``aiohttp.ClientSession`` to reuse.
            When omitted, the client creates and owns its own session.
    """

    def __init__(
        self,
        auth_token: str,
        user_agent: str = DEFAULT_USER_AGENT,
        endpoint: str = DEFAULT_ENDPOINT,
        auto_reconnect: bool = True,
        reconnect_max_delay: float = 60.0,
        heartbeat_interval: Optional[float] = DEFAULT_HEARTBEAT_INTERVAL,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        if not auth_token:
            raise ValueError("auth_token is required")
        self._auth_token = auth_token
        self._user_agent = user_agent
        self._endpoint = endpoint
        self._auto_reconnect = auto_reconnect
        self._reconnect_max_delay = max(0.0, reconnect_max_delay)
        self._heartbeat_interval = heartbeat_interval

        self._session = session
        self._owned_session = session is None

        self._ws: Optional[aiohttp.ClientWebSocketResponse] = None
        self._receiver_task: Optional[asyncio.Task] = None
        self._heartbeat_task: Optional[asyncio.Task] = None
        self._closed = False
        self._queue: "asyncio.Queue[Any]" = asyncio.Queue()

        #: event-type -> list of async handlers
        self._handlers: Dict[str, List[Callable[..., Any]]] = {}
        self._event_handlers: List[Callable[..., Any]] = []
        self._error_handlers: List[Callable[..., Any]] = []
        self._connect_handlers: List[Callable[..., Any]] = []
        self._disconnect_handlers: List[Callable[..., Any]] = []
        self._reconnect_handlers: List[Callable[..., Any]] = []

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @classmethod
    def from_client(cls, api_client, **kwargs) -> "VRChatWebSocket":
        """Build a client from a logged-in ``ApiClient``.

        Reads the ``auth`` cookie from the client's cookie jar and inherits
        its ``User-Agent``. ``kwargs`` are forwarded to the constructor.
        """
        auth_token = get_auth_cookie(api_client)
        if auth_token is None:
            raise ValueError(
                "no 'auth' cookie found; log in with the API client first "
                "(e.g. call get_current_user())"
            )
        kwargs.setdefault("user_agent", getattr(api_client, "user_agent", DEFAULT_USER_AGENT))
        return cls(auth_token=auth_token, **kwargs)

    @property
    def is_connected(self) -> bool:
        ws = self._ws
        return ws is not None and not ws.closed

    def on(
        self, event_type: str, handler: Optional[Callable[..., Any]] = None
    ) -> Callable[..., Any]:
        """Register ``handler`` for ``event_type``.

        Works both directly (``ws.on("x", handler)``) and as a decorator
        (``@ws.on("x")``); in both cases the handler is returned.
        """
        if handler is None:

            def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
                self._handlers.setdefault(event_type, []).append(fn)
                return fn

            return decorator
        self._handlers.setdefault(event_type, []).append(handler)
        return handler

    def off(self, event_type: str, handler: Callable[..., Any]) -> None:
        """Remove a previously registered event handler."""
        handlers = self._handlers.get(event_type)
        if handlers is not None and handler in handlers:
            handlers.remove(handler)

    def on_event(self, handler: Callable[..., Any]) -> Callable[..., Any]:
        """Register a catch-all handler invoked for every event."""
        self._event_handlers.append(handler)
        return handler

    def on_error(self, handler: Callable[..., Any]) -> Callable[..., Any]:
        """Register a handler invoked with an ``Exception`` on pipeline errors."""
        self._error_handlers.append(handler)
        return handler

    def on_connect(self, handler: Callable[..., Any]) -> Callable[..., Any]:
        """Register a handler invoked (no arguments) after connecting."""
        self._connect_handlers.append(handler)
        return handler

    def on_disconnect(self, handler: Callable[..., Any]) -> Callable[..., Any]:
        """Register a handler invoked (no arguments) after disconnecting."""
        self._disconnect_handlers.append(handler)
        return handler

    def on_reconnect(self, handler: Callable[..., Any]) -> Callable[..., Any]:
        """Register a handler invoked with the backoff delay (seconds) before reconnecting."""
        self._reconnect_handlers.append(handler)
        return handler

    async def connect(self) -> None:
        """Establish a single connection and start the background receiver.

        Intended for iterator-style consumption::

            await ws.connect()
            async for event in ws:
                ...
            await ws.close()

        For automatic reconnection use :meth:`run` instead.
        """
        if self.is_connected:
            return
        await self._connect_once()
        self._ensure_receiver()

    async def run(self) -> None:
        """Run the receive loop until :meth:`close` or (without auto-reconnect)
        until the connection is closed.

        Connects if needed, dispatches events to callbacks and the shared
        queue, and reconnects with exponential backoff when
        ``auto_reconnect`` is enabled.
        """
        attempt = 0
        while not self._closed:
            if not self.is_connected:
                try:
                    await self._connect_once()
                    attempt = 0
                except asyncio.CancelledError:
                    raise
                except Exception as exc:
                    await self._fire(self._error_handlers, exc)
                    if not await self._wait_before_reconnect(attempt):
                        break
                    attempt += 1
                    continue

            self._ensure_receiver()
            try:
                await self._receiver_task
            except asyncio.CancelledError:
                if not self._closed:
                    raise
            finally:
                await self._teardown()

            if self._closed or not self._auto_reconnect:
                break
            if not await self._wait_before_reconnect(attempt):
                break
            attempt += 1

        self._put_end()
        # run() is done for good: release the session we own so connections
        # do not linger. (close() already closed it in that path.)
        if self._owned_session and self._session is not None:
            try:
                await self._session.close()
            except Exception:
                pass
            self._session = None

    async def close(self) -> None:
        """Close the connection and stop the receiver; safe to call twice."""
        if self._closed:
            return
        self._closed = True
        self._put_end()

        heartbeat_task = self._heartbeat_task
        self._heartbeat_task = None
        if (
            heartbeat_task is not None
            and heartbeat_task is not asyncio.current_task()
            and not heartbeat_task.done()
        ):
            heartbeat_task.cancel()
            try:
                await heartbeat_task
            except (asyncio.CancelledError, Exception):
                pass

        receiver_task = self._receiver_task
        if (
            receiver_task is not None
            and receiver_task is not asyncio.current_task()
            and not receiver_task.done()
        ):
            receiver_task.cancel()
            try:
                await receiver_task
            except (asyncio.CancelledError, Exception):
                pass

        ws = self._ws
        self._ws = None
        if ws is not None and not ws.closed:
            try:
                await ws.close()
            except Exception:
                pass

        if self._owned_session and self._session is not None:
            try:
                await self._session.close()
            except Exception:
                pass
            self._session = None

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    async def _connect_once(self) -> None:
        if self.is_connected:
            return

        session = self._session
        if session is None:
            session = aiohttp.ClientSession(trust_env=False)
            self._session = session
            self._owned_session = True

        url = f"{self._endpoint.rstrip('/')}/?authToken={quote(self._auth_token, safe='')}"
        headers = {"User-Agent": self._user_agent}
        try:
            ws = await session.ws_connect(url, headers=headers)
        except Exception:
            # Do not leak a freshly-created session on a failed connect;
            # close it so callers do not accumulate resources.
            if self._owned_session and session is self._session:
                await session.close()
                self._session = None
            raise

        self._ws = ws
        if self._heartbeat_interval is not None:
            self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())
        await self._fire(self._connect_handlers)

    def _ensure_receiver(self) -> None:
        if self._receiver_task is None or self._receiver_task.done():
            self._receiver_task = asyncio.create_task(self._receive_loop())

    async def _receive_loop(self) -> None:
        ws = self._ws
        try:
            async for message in ws:
                if message.type == aiohttp.WSMsgType.TEXT:
                    if not await self._dispatch_message(message.data):
                        break
                elif message.type == aiohttp.WSMsgType.ERROR:
                    exc = ws.exception()
                    raise RuntimeError(f"websocket error: {exc}")
                elif message.type in (
                    aiohttp.WSMsgType.CLOSE,
                    aiohttp.WSMsgType.CLOSING,
                    aiohttp.WSMsgType.CLOSED,
                ):
                    break
                # BINARY and other frames are ignored.
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            await self._fire(self._error_handlers, exc)
        finally:
            await self._fire(self._disconnect_handlers)

    async def _dispatch_message(self, raw: str) -> bool:
        """Decode and dispatch one text frame.

        Returns ``False`` when the connection should be closed (a server
        error message was received); ``True`` otherwise.
        """
        try:
            obj = json.loads(raw)
        except (ValueError, TypeError) as exc:
            await self._fire(self._error_handlers, exc)
            return True
        if not isinstance(obj, dict):
            await self._fire(
                self._error_handlers,
                ValueError(f"unexpected pipeline message shape: {type(obj).__name__}"),
            )
            return True

        # Server error messages look like {"err": "..."} and the connection
        # is closed right after they are sent.
        if "err" in obj:
            await self._fire(
                self._error_handlers, VRChatWebSocketError(str(obj["err"]), raw=raw)
            )
            return False

        msg_type = obj.get("type")
        raw_content = obj.get("content")
        content: Any = None

        if msg_type in _NO_CONTENT_EVENTS:
            raw_content = None
        elif msg_type in _STRING_CONTENT_EVENTS:
            content = raw_content
        elif raw_content is not None:
            try:
                content = json.loads(raw_content)
            except (ValueError, TypeError):
                await self._fire(
                    self._error_handlers,
                    VRChatWebSocketError(
                        f"failed to decode content for {msg_type!r}", raw=raw
                    ),
                )
                return True

        event = VRChatEvent(
            type=msg_type, content=content, raw=raw, raw_content=raw_content
        )
        for handler in list(self._handlers.get(msg_type, ())):
            await self._invoke(handler, event)
        for handler in list(self._event_handlers):
            await self._invoke(handler, event)
        self._queue.put_nowait(event)
        return True

    async def _heartbeat_loop(self) -> None:
        try:
            while True:
                await asyncio.sleep(self._heartbeat_interval)
                ws = self._ws
                if ws is None or ws.closed:
                    return
                payload = json.dumps(
                    {
                        "type": "heartbeat",
                        "connected": True,
                        "nonce": str(uuid.uuid4()),
                    }
                )
                try:
                    await ws.send_str(payload)
                except Exception:
                    return
        except asyncio.CancelledError:
            raise

    async def _wait_before_reconnect(self, attempt: int) -> bool:
        """Sleep with backoff before reconnecting; ``False`` stops the loop."""
        if self._closed or not self._auto_reconnect:
            return False
        delay = min(self._reconnect_max_delay, 2.0 ** attempt)
        await self._fire(self._reconnect_handlers, delay)
        try:
            await asyncio.sleep(delay)
        except asyncio.CancelledError:
            return False
        return True

    async def _teardown(self) -> None:
        heartbeat_task = self._heartbeat_task
        self._heartbeat_task = None
        if (
            heartbeat_task is not None
            and heartbeat_task is not asyncio.current_task()
            and not heartbeat_task.done()
        ):
            heartbeat_task.cancel()
            try:
                await heartbeat_task
            except (asyncio.CancelledError, Exception):
                pass

        ws = self._ws
        self._ws = None
        if ws is not None and not ws.closed:
            try:
                await ws.close()
            except Exception:
                pass

    def _put_end(self) -> None:
        try:
            self._queue.put_nowait(_END)
        except asyncio.QueueFull:  # pragma: no cover - unbounded queue
            pass

    async def _invoke(self, handler: Callable[..., Any], *args: Any) -> None:
        try:
            result: Any = handler(*args)
            if inspect.isawaitable(result):
                await result
        except asyncio.CancelledError:
            raise
        except Exception:
            logger.exception("Unhandled error in websocket handler %r", handler)

    async def _fire(
        self, handlers: List[Callable[..., Any]], *args: Any
    ) -> None:
        for handler in list(handlers):
            await self._invoke(handler, *args)

    def __aiter__(self):
        return self

    async def __anext__(self):
        item = await self._queue.get()
        if item is _END:
            raise StopAsyncIteration
        return item
