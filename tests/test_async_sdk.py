"""Behavioral tests for the async VRChat API SDK.

The HTTP layer is exercised against a real local aiohttp server so the tests
cover the actual transport (session creation, cookie jar, timeouts). They
verify that the behaviors of the original synchronous SDK are preserved after
the async conversion:
  - session cookies persist across requests (login flow)
  - 2FA required responses raise readable UnauthorizedException
  - HTTP status codes map to the dedicated exception classes
  - boolean query parameters serialize as true/false
  - path parameters are URL-encoded with the safe charset ~()
  - basic auth credentials are URL-encoded
  - request timeouts map to aiohttp.ClientTimeout
"""

import asyncio
import base64
import json
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

import aiohttp
from multidict import CIMultiDict

import pytest
from aiohttp import web

import vrchatapi
from vrchatapi import ApiClient, Configuration
from vrchatapi.api import authentication_api
from vrchatapi.exceptions import (
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    ServiceException,
    UnauthorizedException,
)


def current_user_payload():
    return {
        "acceptedPrivacyVersion": 5,
        "acceptedTOSVersion": 7,
        "accountDeletionDate": None,
        "accountDeletionLog": None,
        "activeFriends": [],
        "ageVerificationStatus": "18+",
        "ageVerified": True,
        "allowAvatarCopying": False,
        "authToken": None,
        "badges": [],
        "bio": "",
        "bioLinks": [],
        "contentFilters": [],
        "currentAvatar": None,
        "currentAvatarImageUrl": None,
        "currentAvatarTags": [],
        "currentAvatarThumbnailImageUrl": None,
        "date_joined": "2020-01-01T00:00:00.000Z",
        "developerType": "none",
        "discordDetails": None,
        "discordId": None,
        "displayName": "Test",
        "emailVerified": True,
        "friendGroupNames": [],
        "friendKey": None,
        "friends": [],
        "hasBirthday": True,
        "hasEmail": True,
        "hasLoggedInFromClient": True,
        "hasPendingEmail": False,
        "homeLocation": "private",
        "id": "usr_12345678-1234-1234-1234-123456789012",
        "isAdult": True,
        "isFriend": False,
        "last_login": None,
        "last_mobile": None,
        "last_platform": "standalonewindows",
        "obfuscatedEmail": "t***@e.com",
        "obfuscatedPendingEmail": None,
        "oculusId": None,
        "pastDisplayNames": [],
        "profilePicOverride": None,
        "profilePicOverrideThumbnail": None,
        "pronouns": "",
        "pronounsHistory": [],
        "state": "offline",
        "status": "offline",
        "statusDescription": "",
        "statusFirstTime": True,
        "statusHistory": [],
        "steamDetails": None,
        "steamId": None,
        "tags": [],
        "twoFactorAuthEnabled": False,
        "unsubscribe": False,
        "userIcon": None,
        "usesGeneratedPassword": False,
    }


class MockVRCServer:
    """Tiny aiohttp server whose /auth/user behavior is configurable per test."""

    def __init__(self):
        self.seen = []  # (path, headers) for every request
        self.status = 200
        self.body = current_user_payload()
        self.headers = {}
        self.raw_body = None  # when set, sent verbatim
        self.app = web.Application()

        async def handler(request):
            self.seen.append((request.path, request.headers))
            resp = web.Response(status=self.status)
            if self.raw_body is not None:
                resp.text = self.raw_body
                resp.content_type = "application/json"
            else:
                resp.text = json.dumps(self.body)
                resp.content_type = "application/json"
            for k, v in self.headers.items():
                resp.headers[k] = v
            return resp

        self.app.router.add_get("/auth/user", handler)

    async def start(self):
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, "127.0.0.1", 0)
        await self.site.start()
        port = self.site._server.sockets[0].getsockname()[1]
        self.base_url = f"http://127.0.0.1:{port}"

    async def stop(self):
        await self.runner.cleanup()




@pytest.fixture
async def server():
    srv = MockVRCServer()
    await srv.start()
    yield srv
    await srv.stop()


@pytest.mark.asyncio
async def test_login_sends_basic_auth_and_persists_cookie(server):
    config = Configuration(host=server.base_url, username="user+name", password="p@ss:word")
    client = ApiClient(config)
    auth = authentication_api.AuthenticationApi(client)
    server.headers = {"Set-Cookie": "auth=token123; Path=/; Max-Age=3600"}

    user = await auth.get_current_user()
    assert user.display_name == "Test"
    await auth.get_current_user()

    # First request carries URL-encoded basic auth credentials.
    first_auth = server.seen[0][1].get("Authorization")
    assert first_auth is not None and first_auth.startswith("Basic ")
    decoded = base64.b64decode(first_auth.split(" ", 1)[1]).decode()
    assert decoded == "user%2Bname:p%40ss%3Aword"

    # Second request sends the cookie that was stored from the first response.
    assert server.seen[1][1].get("Cookie") == "auth=token123"
    await client.close()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "raw_body,expected_reason",
    [
        ('{"abcdefghijklmnopqrstu":["totp","otp"]}', "2 Factor Authentication verification is required"),
        ('{"abcdefghijklmnopqrstu":["emailOtp"]}', "Email 2 Factor Authentication verification is required"),
    ],
)
async def test_2fa_required_raises_readable_unauthorized(server, raw_body, expected_reason):
    config = Configuration(host=server.base_url)
    client = ApiClient(config)
    auth = authentication_api.AuthenticationApi(client)
    server.raw_body = raw_body

    with pytest.raises(UnauthorizedException) as exc_info:
        await auth.get_current_user()

    assert exc_info.value.status == 200
    assert exc_info.value.reason == expected_reason
    await client.close()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "status,exc_type",
    [
        (401, UnauthorizedException),
        (403, ForbiddenException),
        (404, NotFoundException),
        (500, ServiceException),
        (400, BadRequestException),
    ],
)
async def test_error_status_mapping(server, status, exc_type):
    config = Configuration(host=server.base_url)
    client = ApiClient(config)
    auth = authentication_api.AuthenticationApi(client)
    server.status = status
    server.raw_body = "{}"

    with pytest.raises(exc_type):
        await auth.get_current_user()
    await client.close()


@pytest.mark.asyncio
async def test_boolean_query_params_serialize_lowercase():
    client = ApiClient(Configuration(host="http://localhost"))
    _, url, _, _, _ = await client.param_serialize(
        "GET",
        "/auth/user",
        query_params=[("active", True), ("include", "x")],
    )
    assert "active=true" in url
    assert "active=True" not in url


@pytest.mark.asyncio
async def test_path_params_use_safe_chars():
    client = ApiClient(Configuration(host="http://localhost"))
    _, url, _, _, _ = await client.param_serialize(
        "GET",
        "/users/{userId}",
        path_params=[("userId", "usr_a~b/c d")],
    )
    assert "/users/usr_a~b%2Fc%20d" in url


def test_basic_auth_token_url_encodes_credentials():
    config = Configuration(username="user+name", password="p@ss:word")
    token = config.get_basic_auth_token()
    decoded = base64.b64decode(token.split(" ", 1)[1]).decode()
    assert decoded == "user%2Bname:p%40ss%3Aword"


@pytest.mark.asyncio
async def test_files_parameters_reads_file_off_event_loop(tmp_path: Path):
    upload_file = tmp_path / "upload.txt"
    upload_file.write_bytes(b"upload data")
    client = ApiClient(Configuration(host="http://localhost"))

    with patch("vrchatapi.api_client.asyncio.to_thread", wraps=asyncio.to_thread) as to_thread:
        parameters = await client.files_parameters({"file": str(upload_file)})

    assert parameters == [
        ("file", ("upload.txt", b"upload data", "text/plain"))
    ]
    to_thread.assert_awaited_once_with(client._read_file, str(upload_file))


@pytest.mark.asyncio
async def test_deserialize_file_writes_off_event_loop(tmp_path: Path):
    response = Mock(headers={}, data=b"download data")
    client = ApiClient(Configuration(host="http://localhost"))
    client.configuration.temp_folder_path = str(tmp_path)

    with patch("vrchatapi.api_client.asyncio.to_thread", wraps=asyncio.to_thread) as to_thread:
        path = await client._ApiClient__deserialize_file(response)

    assert Path(path).read_bytes() == b"download data"
    to_thread.assert_awaited_once_with(client._deserialize_file, response)


@pytest.mark.asyncio
async def test_request_timeout_maps_to_client_timeout():
    from vrchatapi import rest as rest_module

    config = Configuration(host="http://localhost")
    rest_client = rest_module.RESTClientObject(config)
    captured = {}

    class FakeResponse:
        status = 200
        reason = "OK"

        def __init__(self):
            self.headers = CIMultiDict()

    class FakeSession:
        async def request(self, **kwargs):
            captured.update(kwargs)
            return FakeResponse()

        async def close(self):
            pass

    rest_client.pool_manager = FakeSession()
    resp = await rest_client.request("GET", "http://localhost/x", _request_timeout=(1.5, 2.5))
    assert isinstance(captured["timeout"], aiohttp.ClientTimeout)
    assert captured["timeout"].connect == 1.5
    assert captured["timeout"].sock_read == 2.5
    assert resp.status == 200

    captured.clear()
    await rest_client.request("GET", "http://localhost/x", _request_timeout=30)
    assert captured["timeout"].total == 30
    await rest_client.close()


@pytest.mark.asyncio
async def test_ssl_context_is_built_lazily_off_the_event_loop(monkeypatch):
    from vrchatapi import rest as rest_module

    config = Configuration(host="http://localhost")
    build_context = Mock()
    monkeypatch.setattr(rest_module.ssl, "create_default_context", build_context)
    build_context.reset_mock()
    rest_client = rest_module.RESTClientObject(config)

    build_context.assert_not_called()

    ssl_context = Mock()
    to_thread = AsyncMock(return_value=ssl_context)
    monkeypatch.setattr(rest_module.asyncio, "to_thread", to_thread)
    monkeypatch.setattr(rest_client, "_create_pool_manager", Mock(return_value=Mock()))

    await rest_client._ensure_session()

    to_thread.assert_awaited_once_with(rest_client._build_ssl_context)
    assert rest_client.ssl_context is ssl_context


@pytest.mark.asyncio
async def test_without_preload_content_returns_raw_response(server):
    config = Configuration(host=server.base_url)
    client = ApiClient(config)
    auth = authentication_api.AuthenticationApi(client)

    raw = await auth.get_current_user_without_preload_content()
    assert isinstance(raw, aiohttp.ClientResponse)
    data = await raw.read()
    assert json.loads(data)["displayName"] == "Test"
    await client.close()


@pytest.mark.asyncio
async def test_async_context_manager_closes_client(server):
    config = Configuration(host=server.base_url)
    async with ApiClient(config) as client:
        auth = authentication_api.AuthenticationApi(client)
        user = await auth.get_current_user()
        assert user.display_name == "Test"
    # Session is closed after exiting the context manager.
    assert client.rest_client.pool_manager.closed
