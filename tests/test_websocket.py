"""Tests for the hand-written VRChat WebSocket (Pipeline) client.

The pipeline is emulated with a real local aiohttp websocket server so the
tests exercise the actual transport (handshake, query authToken, User-Agent,
heartbeat frames, close handling) end to end.
"""

import asyncio
import json
import time
from types import SimpleNamespace

import aiohttp
import pytest
from aiohttp import web

from vrchatapi.websocket import (
    VRChatEvent,
    VRChatWebSocket,
    VRChatWebSocketError,
    get_auth_cookie,
)


def friend_online_frame(user_id="usr_x", display_name="Alice"):
    return json.dumps(
        {
            "type": "friend-online",
            "content": json.dumps(
                {
                    "user": {
                        "id": user_id,
                        "displayName": display_name,
                        "location": "offline",
                    }
                }
            ),
        }
    )


def notification_frame():
    return json.dumps(
        {
            "type": "notification",
            "content": json.dumps(
                {"type": "friendRequest", "senderUserId": "usr_y"}
            ),
        }
    )


class MockPipelineServer:
    """Tiny aiohttp server mimicking the VRChat pipeline websocket."""

    def __init__(self):
        self.connections = []  # (query, headers) per connection
        self.received = []  # text frames sent by the client
        self.frames = []  # frames sent on unscripted connections
        self.close_after_frames = False
        self.script = {}  # connection index -> (frames, close_after_send)
        self.app = web.Application()
        self.app.router.add_get("/", self._ws_handler)

    def set_script(self, conn_index, frames, close_after_send=True):
        self.script[conn_index] = (frames, close_after_send)

    async def start(self):
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, "127.0.0.1", 0)
        await self.site.start()
        port = self.site._server.sockets[0].getsockname()[1]
        self.base_url = f"http://127.0.0.1:{port}"

    async def stop(self):
        await self.runner.cleanup()

    async def _ws_handler(self, request):
        self.connections.append((dict(request.query), request.headers))
        index = len(self.connections) - 1
        frames, close_after = self.script.get(
            index, (self.frames, self.close_after_frames)
        )
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        for frame in frames:
            await ws.send_str(frame)
        if close_after:
            await ws.close()
            return ws
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                self.received.append(msg.data)
            elif msg.type == aiohttp.WSMsgType.ERROR:
                break
            elif msg.type in (aiohttp.WSMsgType.CLOSE, aiohttp.WSMsgType.CLOSED):
                break
        return ws


@pytest.fixture
async def pipeline_server():
    srv = MockPipelineServer()
    await srv.start()
    yield srv
    await srv.stop()


def make_ws(server, **kwargs):
    defaults = dict(
        auth_token="authcookie_test",
        endpoint=server.base_url,
        auto_reconnect=False,
        heartbeat_interval=None,
    )
    defaults.update(kwargs)
    return VRChatWebSocket(**defaults)


# ---------------------------------------------------------------------------
# Connection
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_connect_sends_auth_token_and_user_agent(pipeline_server):
    pipeline_server.set_script(0, [], close_after_send=True)
    ws = VRChatWebSocket(
        auth_token="authcookie_test",
        user_agent="TestApp/1.0 me@example.com",
        endpoint=pipeline_server.base_url,
        auto_reconnect=False,
        heartbeat_interval=None,
    )
    await ws.run()

    query, headers = pipeline_server.connections[0]
    assert query["authToken"] == "authcookie_test"
    assert headers.get("User-Agent") == "TestApp/1.0 me@example.com"


@pytest.mark.asyncio
async def test_auth_token_is_url_encoded(pipeline_server):
    pipeline_server.set_script(0, [], close_after_send=True)
    token = "authcookie_a b&c=d"
    ws = VRChatWebSocket(
        auth_token=token,
        endpoint=pipeline_server.base_url,
        auto_reconnect=False,
        heartbeat_interval=None,
    )
    await ws.run()

    # The server sees the decoded original token; without URL encoding the
    # unquoted "&" / "=" would have split the query string.
    query, _ = pipeline_server.connections[0]
    assert query["authToken"] == token


# ---------------------------------------------------------------------------
# Decoding
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_content_decoding_matrix():
    ws = VRChatWebSocket(auth_token="x", heartbeat_interval=None)
    seen = []

    @ws.on_event
    async def on_event(event):
        seen.append(event)

    def frame(msg_type, content=None):
        payload = {"type": msg_type}
        if content is not None:
            payload["content"] = content
        return json.dumps(payload)

    assert (
        await ws._dispatch_message(
            frame("notification", json.dumps({"type": "friendRequest", "senderUserId": "usr_x"}))
        )
        is True
    )
    assert await ws._dispatch_message(frame("see-notification", "not_abc")) is True
    assert await ws._dispatch_message(frame("clear-notification")) is True
    assert (
        await ws._dispatch_message(
            frame("notification-v2-delete", json.dumps({"notificationIds": ["n1", "n2"]}))
        )
        is True
    )

    assert [e.type for e in seen] == [
        "notification",
        "see-notification",
        "clear-notification",
        "notification-v2-delete",
    ]
    assert seen[0].content == {"type": "friendRequest", "senderUserId": "usr_x"}
    assert isinstance(seen[0], VRChatEvent)
    assert seen[1].content == "not_abc"
    assert seen[1].raw_content == "not_abc"
    assert seen[2].content is None
    assert seen[2].raw_content is None
    assert seen[3].content == {"notificationIds": ["n1", "n2"]}


@pytest.mark.asyncio
async def test_malformed_content_reports_error_and_keeps_connection():
    ws = VRChatWebSocket(auth_token="x", heartbeat_interval=None)
    errors = []

    @ws.on_error
    async def on_error(exc):
        errors.append(exc)

    # content is not valid JSON but the connection itself stays up.
    assert await ws._dispatch_message('{"type":"notification","content":"nope"}') is True
    assert len(errors) == 1
    assert isinstance(errors[0], VRChatWebSocketError)


@pytest.mark.asyncio
async def test_server_error_message_closes_connection():
    ws = VRChatWebSocket(auth_token="x", heartbeat_interval=None)
    errors = []

    @ws.on_error
    async def on_error(exc):
        errors.append(exc)

    assert await ws._dispatch_message('{"err":"Error finding user usr_x"}') is False
    assert len(errors) == 1
    assert isinstance(errors[0], VRChatWebSocketError)
    assert "Error finding user" in str(errors[0])
    assert errors[0].raw == '{"err":"Error finding user usr_x"}'


# ---------------------------------------------------------------------------
# Callbacks
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_callback_dispatch_and_catch_all(pipeline_server):
    pipeline_server.set_script(
        0, [friend_online_frame(), notification_frame()], close_after_send=True
    )
    ws = make_ws(pipeline_server)
    typed, catch_all = [], []

    @ws.on("friend-online")
    async def on_friend_online(event):
        typed.append(event.content["user"]["displayName"])

    @ws.on_event
    async def on_event(event):
        catch_all.append(event.type)

    await ws.run()

    assert typed == ["Alice"]
    assert catch_all == ["friend-online", "notification"]


@pytest.mark.asyncio
async def test_off_removes_handler(pipeline_server):
    pipeline_server.set_script(0, [friend_online_frame()], close_after_send=True)
    ws = make_ws(pipeline_server)
    calls = []

    @ws.on("friend-online")
    async def handler(event):
        calls.append(event)

    ws.off("friend-online", handler)
    await ws.run()

    assert calls == []


# ---------------------------------------------------------------------------
# Async iterator
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_async_iterator_yields_events(pipeline_server):
    pipeline_server.set_script(
        0, [friend_online_frame(), notification_frame()], close_after_send=False
    )
    ws = make_ws(pipeline_server)
    await ws.connect()

    collected = []

    async def consume():
        async for event in ws:
            collected.append(event.type)
            if len(collected) == 2:
                await ws.close()

    await consume()

    assert collected == ["friend-online", "notification"]


@pytest.mark.asyncio
async def test_async_iterator_stops_on_disconnect(pipeline_server):
    pipeline_server.set_script(
        0, [friend_online_frame(), notification_frame()], close_after_send=True
    )
    ws = make_ws(pipeline_server)
    await ws.connect()

    collected = []
    async for event in ws:
        collected.append(event.type)

    assert collected == ["friend-online", "notification"]
    assert not ws.is_connected


# ---------------------------------------------------------------------------
# Errors / lifecycle
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_server_error_ends_run(pipeline_server):
    pipeline_server.set_script(
        0, ['{"err":"Error finding user usr_x"}'], close_after_send=True
    )
    ws = make_ws(pipeline_server)
    errors = []

    @ws.on_error
    async def on_error(exc):
        errors.append(exc)

    await ws.run()

    assert len(errors) == 1
    assert isinstance(errors[0], VRChatWebSocketError)
    assert not ws.is_connected


# ---------------------------------------------------------------------------
# Heartbeat
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_heartbeat_frames_are_sent(pipeline_server):
    pipeline_server.set_script(0, [], close_after_send=False)
    ws = make_ws(pipeline_server, heartbeat_interval=0.05)

    task = asyncio.create_task(ws.run())
    try:
        deadline = time.monotonic() + 10
        while not pipeline_server.received and time.monotonic() < deadline:
            await asyncio.sleep(0.02)
    finally:
        await ws.close()
        await task

    assert pipeline_server.received, "server never received a heartbeat frame"
    heartbeats = [
        json.loads(frame)
        for frame in pipeline_server.received
        if json.loads(frame).get("type") == "heartbeat"
    ]
    assert heartbeats, pipeline_server.received
    assert heartbeats[0]["connected"] is True
    assert heartbeats[0]["nonce"]


# ---------------------------------------------------------------------------
# Reconnect
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_auto_reconnect_after_drop(pipeline_server):
    # First connection drops immediately; the client must reconnect and
    # receive the event sent on the second connection.
    pipeline_server.set_script(0, [], close_after_send=True)
    pipeline_server.set_script(1, [friend_online_frame()], close_after_send=False)

    ws = make_ws(
        pipeline_server,
        auto_reconnect=True,
        reconnect_max_delay=0.05,
    )
    received = []
    got = asyncio.Event()
    reconnects = []

    @ws.on("friend-online")
    async def on_friend_online(event):
        received.append(event.content["user"]["displayName"])
        got.set()

    @ws.on_reconnect
    async def on_reconnect(delay):
        reconnects.append(delay)

    task = asyncio.create_task(ws.run())
    try:
        await asyncio.wait_for(got.wait(), timeout=10)
    finally:
        await ws.close()
        await task

    assert len(pipeline_server.connections) >= 2
    assert received == ["Alice"]
    assert reconnects


# ---------------------------------------------------------------------------
# from_client / auth cookie
# ---------------------------------------------------------------------------


class _FakeCookieJar:
    def __init__(self, cookies):
        self._cookies = cookies

    def __iter__(self):
        return iter(self._cookies)


class _FakeApiClient:
    def __init__(self, cookies, user_agent="MyApp/1.0 me@example.com"):
        self.rest_client = SimpleNamespace(cookie_jar=_FakeCookieJar(cookies))
        self.user_agent = user_agent


def test_from_client_reads_auth_cookie_and_user_agent():
    client = _FakeApiClient(
        [
            SimpleNamespace(name="twoFactorAuth", value="2fa-value"),
            SimpleNamespace(name="auth", value="authcookie_123"),
        ]
    )
    ws = VRChatWebSocket.from_client(client)
    assert ws._auth_token == "authcookie_123"
    assert ws._user_agent == "MyApp/1.0 me@example.com"


def test_from_client_raises_without_auth_cookie():
    client = _FakeApiClient([])
    with pytest.raises(ValueError, match="auth"):
        VRChatWebSocket.from_client(client)


def test_get_auth_cookie_returns_none_without_rest_client():
    assert get_auth_cookie(SimpleNamespace()) is None


def test_constructor_requires_auth_token():
    with pytest.raises(ValueError, match="auth_token"):
        VRChatWebSocket(auth_token="")
