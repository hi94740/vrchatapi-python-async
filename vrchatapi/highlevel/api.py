"""Dictionary-based VRChat API preserving partial and unknown response fields."""

from __future__ import annotations

from collections.abc import Mapping
from enum import Enum
from functools import cached_property
from http.cookiejar import Cookie
import json
from typing import cast
from urllib.parse import urlsplit

import vrchatapi
from vrchatapi.websocket import DEFAULT_USER_AGENT, VRChatWebSocket

from .types import CurrentUser, User, VRChatAuthCookie, World

CONF_COOKIE_AUTH = "auth"
CONF_COOKIE_2FA = "twoFactorAuth"


class TwoFactorAuthChallenge(str, Enum):
    """Supported two-factor authentication challenges."""

    TOTP = "totp"
    EMAIL_OTP = "emailOtp"


class TwoFactorAuthRequired(vrchatapi.exceptions.UnauthorizedException):
    """Authentication requires a code for the indicated challenge."""

    def __init__(self, challenge: TwoFactorAuthChallenge, *, http_resp=None) -> None:
        self.challenge = challenge
        super().__init__(
            status=200,
            reason="Two-factor authentication required",
            http_resp=http_resp,
        )


class _DictionaryApiClient(vrchatapi.ApiClient):
    """Use the SDK's authentication/error handling without lossy model conversion."""

    async def response_deserialize(self, response_data, response_types_map=None):
        if response_data.status == 200 and response_data.data:
            try:
                payload = json.loads(response_data.data)
            except ValueError:
                payload = None
            if isinstance(payload, dict) and "requiresTwoFactorAuth" in payload:
                methods = payload["requiresTwoFactorAuth"]
                if isinstance(methods, list):
                    for challenge in (
                        TwoFactorAuthChallenge.EMAIL_OTP,
                        TwoFactorAuthChallenge.TOTP,
                    ):
                        if challenge.value in methods:
                            raise TwoFactorAuthRequired(
                                challenge, http_resp=response_data
                            )
                raise vrchatapi.exceptions.UnauthorizedException(
                    http_resp=response_data,
                    reason="Unsupported two-factor authentication challenge",
                )
        response_types_map = dict(response_types_map or {})
        if 200 <= response_data.status < 300:
            response_types_map[str(response_data.status)] = "object"
        return await super().response_deserialize(response_data, response_types_map)


class VRChatAPI:
    """Own an authenticated REST client and its pipeline connections."""

    def __init__(
        self,
        config: Mapping[str, str] | None = None,
        cookie: VRChatAuthCookie | None = None,
        *,
        user_agent: str = DEFAULT_USER_AGENT,
    ) -> None:
        self.config = dict(config or {})
        self.api_client = _DictionaryApiClient(
            vrchatapi.Configuration(
                username=self.config.get("username"),
                password=self.config.get("password"),
            )
        )
        self.api_client.user_agent = user_agent
        self._websockets: list[VRChatWebSocket] = []
        self._closed = False
        self.cookie = cookie

    @property
    def cookie(self) -> VRChatAuthCookie:
        return get_cookie_dict(self.api_client)

    @cookie.setter
    def cookie(self, value: VRChatAuthCookie | None) -> None:
        set_cookie_dict(self.api_client, value)

    def clear_cookie(self) -> None:
        self.api_client.rest_client.cookie_jar.clear()

    def copy(self) -> VRChatAPI:
        return VRChatAPI(
            self.config, self.cookie, user_agent=self.api_client.user_agent
        )

    @cached_property
    def auth_api(self) -> vrchatapi.AuthenticationApi:
        return vrchatapi.AuthenticationApi(self.api_client)

    @cached_property
    def friends_api(self) -> vrchatapi.FriendsApi:
        return vrchatapi.FriendsApi(self.api_client)

    @cached_property
    def users_api(self) -> vrchatapi.UsersApi:
        return vrchatapi.UsersApi(self.api_client)

    @cached_property
    def worlds_api(self) -> vrchatapi.WorldsApi:
        return vrchatapi.WorldsApi(self.api_client)

    async def get_current_user(self) -> CurrentUser:
        return cast(CurrentUser, await self.auth_api.get_current_user())

    async def verify2_fa(self, code: str):
        return await self.auth_api.verify2_fa(vrchatapi.TwoFactorAuthCode(code=code))

    async def verify2_fa_email_code(self, code: str):
        return await self.auth_api.verify2_fa_email_code(
            vrchatapi.TwoFactorEmailCode(code=code)
        )

    async def get_friends(self, offset: int, n: int, offline: bool) -> list[User]:
        return cast(
            list[User],
            await self.friends_api.get_friends(offset=offset, n=n, offline=offline),
        )

    async def get_user(self, user_id: str) -> User:
        return cast(User, await self.users_api.get_user(user_id))

    async def update_user(
        self, user_id: str, data: vrchatapi.UpdateUserRequest
    ) -> CurrentUser:
        return cast(
            CurrentUser,
            await self.users_api.update_user(user_id, update_user_request=data),
        )

    async def get_world(self, world_id: str) -> World:
        return cast(World, await self.worlds_api.get_world(world_id))

    async def ws_connect(self) -> VRChatWebSocket:
        # The account owns authentication recovery and reconnect snapshots.
        ws = VRChatWebSocket.from_client(self.api_client, auto_reconnect=False)
        try:
            await ws.connect()
        except BaseException:
            await ws.close()
            raise
        self._websockets.append(ws)
        return ws

    async def logout(self):
        return await self.auth_api.logout()

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        try:
            for ws in self._websockets:
                await ws.close()
        finally:
            self._websockets.clear()
            await self.api_client.close()

    async def __aenter__(self) -> VRChatAPI:
        return self

    async def __aexit__(self, *exc) -> None:
        await self.close()


def make_cookie(name: str, value: str, domain: str) -> Cookie:
    return Cookie(
        0,
        name,
        value,
        None,
        False,
        domain,
        True,
        False,
        "/",
        False,
        False,
        None,
        False,
        None,
        None,
        {},
    )


def set_cookie_dict(
    api: vrchatapi.ApiClient, cookie: VRChatAuthCookie | None = None
) -> None:
    domain = urlsplit(api.configuration.host).hostname
    if domain is None:
        raise ValueError(f"Invalid API host: {api.configuration.host!r}")
    for name in (CONF_COOKIE_AUTH, CONF_COOKIE_2FA):
        if cookie and (value := cookie.get(name)):
            api.rest_client.cookie_jar.set_cookie(make_cookie(name, value, domain))


def get_cookie_dict(api: vrchatapi.ApiClient) -> VRChatAuthCookie:
    domain = urlsplit(api.configuration.host).hostname
    if domain is None:
        raise ValueError(f"Invalid API host: {api.configuration.host!r}")
    return cast(
        VRChatAuthCookie,
        {
            cookie.name: cookie.value
            for cookie in api.rest_client.cookie_jar
            if cookie.domain == domain
            and cookie.path == "/"
            and cookie.name in (CONF_COOKIE_AUTH, CONF_COOKIE_2FA)
            and cookie.value
        },
    )
