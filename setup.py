"""
    VRChat API Documentation

![](https://github.com/vrchatapi/vrchatapi.github.io/blob/main/static/assets/img/lang/lang_python_banner_1500x300.png?raw=true)

# VRChat API Library for Python (async)

A Python client to interact with the unofficial VRChat API. Supports all REST calls specified in the [API specification](https://github.com/vrchatapi/specification).

This is an **asynchronous** (asyncio + aiohttp) adaptation of [VRChatAPI-Python](https://github.com/vrchatapi/vrchatapi-python). All API
methods are coroutines and must be awaited.

## Disclaimer

This is the official response of the VRChat Team (from Tupper more specifically) on the usage of the VRChat API.

> Use of the API using applications other than the approved methods (website, VRChat application) are not officially supported. You may use the API for your own application, but keep these guidelines in mind:
> * We do not provide documentation or support for the API.
> * Do not make queries to the API more than once per 60 seconds.
> * Abuse of the API may result in account termination.
> * Access to API endpoints may break at any given time, with no warning.

As stated, this documentation was not created with the help of the official VRChat team. Therefore this documentation is not an official documentation of the VRChat API and may not be always up to date with the latest versions. If you find that a page or endpoint is not longer valid please create an issue and tell us so we can fix it.

## Getting Started

First add the package to to your project:
```bash
pip install vrchatapi-async
```

Below is an example on how to login to the API and fetch your own user information.

```python
import asyncio

# Step 1. We begin with creating a Configuration, which contains the username and password for authentication.
import vrchatapi
from vrchatapi.api import authentication_api
from vrchatapi.exceptions import UnauthorizedException
from vrchatapi.models.two_factor_auth_code import TwoFactorAuthCode
from vrchatapi.models.two_factor_email_code import TwoFactorEmailCode


async def main():
    configuration = vrchatapi.Configuration(
        username = 'username',
        password = 'password',
    )

    # Step 2. VRChat consists of several API's (WorldsApi, UsersApi, FilesApi, NotificationsApi, FriendsApi, etc...)
    # Here we enter a context of the API Client and instantiate the Authentication API which is required for logging in.

    # Enter a context with an instance of the API client
    async with vrchatapi.ApiClient(configuration) as api_client:
        # Set our User-Agent as per VRChat Usage Policy
        api_client.user_agent = "ExampleProgram/0.0.1 my@email.com"

        # Instantiate instances of API classes
        auth_api = authentication_api.AuthenticationApi(api_client)

        try:
            # Step 3. Calling getCurrentUser on Authentication API logs you in if the user isn't already logged in.
            current_user = await auth_api.get_current_user()
        except UnauthorizedException as e:
            if e.status == 200:
                if "Email 2 Factor Authentication" in e.reason:
                    # Step 3.5. Calling email verify2fa if the account has 2FA disabled
                    await auth_api.verify2_fa_email_code(two_factor_email_code=TwoFactorEmailCode(input("Email 2FA Code: ")))
                elif "2 Factor Authentication" in e.reason:
                    # Step 3.5. Calling verify2fa if the account has 2FA enabled
                    await auth_api.verify2_fa(two_factor_auth_code=TwoFactorAuthCode(input("2FA Code: ")))
                current_user = await auth_api.get_current_user()
            else:
                print("Exception when calling API: %s\n", e)
        except vrchatapi.ApiException as e:
            print("Exception when calling API: %s\n", e)

        print("Logged in as:", current_user.display_name)


if __name__ == "__main__":
    asyncio.run(main())
```

See [Examples](examples/README.md) for more example usage on getting started.

## Async API notes

Compared to [the synchronous SDK](https://github.com/vrchatapi/vrchatapi-python), this version changes the calling convention:

- Every API method (`foo`, `foo_with_http_info`, `foo_without_preload_content`)
  is an `async def` coroutine and must be awaited.
- `ApiClient` is used as an async context manager (`async with ... as api_client`).
- The `async_req` parameter and the thread-pool based `async_req=True` usage are
  removed; calls are natively asynchronous.
- `foo_with_http_info()` returns an `ApiResponse` object (`status_code`,
  `headers`, `data`, `raw_data`) instead of a `(data, status, headers)` tuple.
- `foo_without_preload_content()` returns the raw aiohttp response for
  streaming; the legacy `_preload_content=False` parameter is removed.
- The session `CookieJar`, the readable 2FA errors
  (`UnauthorizedException` with status 200), the URL-encoded basic auth, the
  `~()` safe path-parameter charset and the lowercase boolean query parameters
  behave exactly like the synchronous SDK.

## Contributing

Contributions are welcome, but do not add features that should be handled by the OpenAPI specification.

## Websocket (Pipeline) API

The SDK also ships a hand-written async client for VRChat's real-time
WebSocket (Pipeline) API (`wss://pipeline.vrchat.cloud`), which pushes invites,
friend requests, friend online/offline events, user and group updates to the
authenticated client. The connection is receive-only; every message's
double-encoded `content` field is automatically unpacked into a plain dict.

```python
import asyncio

import vrchatapi
from vrchatapi.api import authentication_api
from vrchatapi.websocket import VRChatWebSocket


async def main():
    configuration = vrchatapi.Configuration(username="username", password="password")
    async with vrchatapi.ApiClient(configuration) as api_client:
        api_client.user_agent = "ExampleProgram/0.0.1 my@email.com"
        await authentication_api.AuthenticationApi(api_client).get_current_user()

        # Reads the auth cookie + User-Agent from the logged-in client.
        ws = VRChatWebSocket.from_client(api_client)

        @ws.on("friend-online")
        async def on_friend_online(event):
            print("online:", event.content["user"]["displayName"])

        # Or consume the same stream as an async iterator:
        #   async for event in ws:
        #       print(event.type, event.content)

        await ws.run()  # blocks; reconnects automatically by default
```

`VRChatWebSocket` supports callback registration (`ws.on("friend-online", ...)`
/ `@ws.on(...)`, a catch-all `ws.on_event(...)`), an async iterator over the
same event stream, error/connect/disconnect/reconnect hooks, automatic
reconnection with exponential backoff (`auto_reconnect=False` disables it), and
a configurable application-level heartbeat (default 30s;
`heartbeat_interval=None` disables it). See
[examples/examples-source/websocket.py](examples/examples-source/websocket.py)
and the [Websocket API reference](https://vrchat.community/websocket) for
details.

## High-level account API

`vrchatapi.highlevel` adds a dictionary-based API and a live account snapshot.
The existing generated model-based API remains unchanged. Responses retain
unknown fields, explicit nulls and missing fields, including partial updates.

```python
from vrchatapi.highlevel import VRChatAPI, VRChatAccount

api = VRChatAPI(
    {"username": "user", "password": "password"},
    user_agent="MyApplication/1.0 contact@example.com",
)
# get_current_user and verify2_fa / verify2_fa_email_code can also be used
# separately for interactive authentication. Persist api.cookie in your app.
current_user = await api.get_current_user()
account = VRChatAccount(
    api,
    current_user["id"],
    on_user=lambda user, world_changed: print(user.id, user.data),
    on_remove=lambda user_id: print("Removed", user_id),
    on_available=lambda available: print("Connected", available),
)
try:
    await account.start(current_user)
    # Keep your application's event loop running while using account.users.
finally:
    await account.close()
```

For interactive login, catch `vrchatapi.highlevel.TwoFactorAuthRequired` and
branch on its `challenge`: `TwoFactorAuthChallenge.EMAIL_OTP` uses
`verify2_fa_email_code`, while `TwoFactorAuthChallenge.TOTP` uses `verify2_fa`.
Then call `get_current_user` again. Classification uses the response's
`requiresTwoFactorAuth` field, independent of exception wording. The exception
is also an `UnauthorizedException`; unsupported challenges remain ordinary
`UnauthorizedException` errors.

The account owns its REST client, pipeline and default world cache. It fetches
friend pages, resolves missing users, applies pipeline changes in receive order,
and refreshes authentication and snapshots after disconnection. Authentication
failures are exposed through `on_auth_error`; initial setup errors are raised.
`on_authenticated` is an optional async callback for saving `api.cookie`.
Other callbacks are synchronous and must not block the event loop.

Each account has its own world cache by default. For deliberate sharing, pass
an explicit `WorldCache(fetch_world)` to multiple accounts and close it after
all consumers stop. A caller-supplied cache is never closed by an account.

`WorldCache.sorted_names` returns a cached, sorted tuple of unique names from
loaded worlds without fetching metadata. Update metadata with `cache.get(id, data)`
or assignment to `world.data`; in-place changes to the data dictionary or direct
mutation of `cache.registry` bypass name-cache invalidation. Name changes, cache
additions, pruning, and closure invalidate or clear the cached result.
World requests are deduplicated; cancelling one waiter does not cancel other
waiters. Closing the owner cancels pending fetches and retries.

The source of this API lives in `client/highlevel/`. `generate.sh` copies it to
`vrchatapi/highlevel/` after regeneration; edit the source, not the shipped copy.
`tools/stamp_version.py VERSION` stamps local release builds using the same
version step as generation. Release `1.21.0` includes this API.

    The version of the OpenAPI document: 1.21.0
    Contact: vrchatapi.lpv0t@aries.fyi
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "vrchatapi-async"
VERSION = "1.21.0"
PYTHON_REQUIRES = ">= 3.10"
REQUIRES = [
    "python-dateutil >= 2.8.2",
    "aiohttp >= 3.13.5",
    "aiohttp-retry >= 2.8.3",
    "pydantic >= 2.11",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="VRChat API Library for Python (async version)",
    author="hi94740",
    author_email="hi94740@qq.com",
    url="https://github.com/hi94740/vrchatapi-python-async",
    keywords=["vrchat", "vrchatapi", "vrc"],
    install_requires=REQUIRES,
    python_requires=">=3.10",
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description="""\
![](https://github.com/vrchatapi/vrchatapi.github.io/blob/main/static/assets/img/lang/lang_python_banner_1500x300.png?raw=true)

# VRChat API Library for Python (async)

A Python client to interact with the unofficial VRChat API. Supports all REST calls specified in the [API specification](https://github.com/vrchatapi/specification).

This is an **asynchronous** (asyncio + aiohttp) adaptation of [VRChatAPI-Python](https://github.com/vrchatapi/vrchatapi-python). All API
methods are coroutines and must be awaited.

## Disclaimer

This is the official response of the VRChat Team (from Tupper more specifically) on the usage of the VRChat API.

> Use of the API using applications other than the approved methods (website, VRChat application) are not officially supported. You may use the API for your own application, but keep these guidelines in mind:
> * We do not provide documentation or support for the API.
> * Do not make queries to the API more than once per 60 seconds.
> * Abuse of the API may result in account termination.
> * Access to API endpoints may break at any given time, with no warning.

As stated, this documentation was not created with the help of the official VRChat team. Therefore this documentation is not an official documentation of the VRChat API and may not be always up to date with the latest versions. If you find that a page or endpoint is not longer valid please create an issue and tell us so we can fix it.

## Getting Started

First add the package to to your project:
```bash
pip install vrchatapi-async
```

Below is an example on how to login to the API and fetch your own user information.

```python
import asyncio

# Step 1. We begin with creating a Configuration, which contains the username and password for authentication.
import vrchatapi
from vrchatapi.api import authentication_api
from vrchatapi.exceptions import UnauthorizedException
from vrchatapi.models.two_factor_auth_code import TwoFactorAuthCode
from vrchatapi.models.two_factor_email_code import TwoFactorEmailCode


async def main():
    configuration = vrchatapi.Configuration(
        username = 'username',
        password = 'password',
    )

    # Step 2. VRChat consists of several API's (WorldsApi, UsersApi, FilesApi, NotificationsApi, FriendsApi, etc...)
    # Here we enter a context of the API Client and instantiate the Authentication API which is required for logging in.

    # Enter a context with an instance of the API client
    async with vrchatapi.ApiClient(configuration) as api_client:
        # Set our User-Agent as per VRChat Usage Policy
        api_client.user_agent = "ExampleProgram/0.0.1 my@email.com"

        # Instantiate instances of API classes
        auth_api = authentication_api.AuthenticationApi(api_client)

        try:
            # Step 3. Calling getCurrentUser on Authentication API logs you in if the user isn't already logged in.
            current_user = await auth_api.get_current_user()
        except UnauthorizedException as e:
            if e.status == 200:
                if "Email 2 Factor Authentication" in e.reason:
                    # Step 3.5. Calling email verify2fa if the account has 2FA disabled
                    await auth_api.verify2_fa_email_code(two_factor_email_code=TwoFactorEmailCode(input("Email 2FA Code: ")))
                elif "2 Factor Authentication" in e.reason:
                    # Step 3.5. Calling verify2fa if the account has 2FA enabled
                    await auth_api.verify2_fa(two_factor_auth_code=TwoFactorAuthCode(input("2FA Code: ")))
                current_user = await auth_api.get_current_user()
            else:
                print("Exception when calling API: %s\n", e)
        except vrchatapi.ApiException as e:
            print("Exception when calling API: %s\n", e)

        print("Logged in as:", current_user.display_name)


if __name__ == "__main__":
    asyncio.run(main())
```

See [Examples](examples/README.md) for more example usage on getting started.

## Async API notes

Compared to [the synchronous SDK](https://github.com/vrchatapi/vrchatapi-python), this version changes the calling convention:

- Every API method (`foo`, `foo_with_http_info`, `foo_without_preload_content`)
  is an `async def` coroutine and must be awaited.
- `ApiClient` is used as an async context manager (`async with ... as api_client`).
- The `async_req` parameter and the thread-pool based `async_req=True` usage are
  removed; calls are natively asynchronous.
- `foo_with_http_info()` returns an `ApiResponse` object (`status_code`,
  `headers`, `data`, `raw_data`) instead of a `(data, status, headers)` tuple.
- `foo_without_preload_content()` returns the raw aiohttp response for
  streaming; the legacy `_preload_content=False` parameter is removed.
- The session `CookieJar`, the readable 2FA errors
  (`UnauthorizedException` with status 200), the URL-encoded basic auth, the
  `~()` safe path-parameter charset and the lowercase boolean query parameters
  behave exactly like the synchronous SDK.

## Contributing

Contributions are welcome, but do not add features that should be handled by the OpenAPI specification.

## Websocket (Pipeline) API

The SDK also ships a hand-written async client for VRChat's real-time
WebSocket (Pipeline) API (`wss://pipeline.vrchat.cloud`), which pushes invites,
friend requests, friend online/offline events, user and group updates to the
authenticated client. The connection is receive-only; every message's
double-encoded `content` field is automatically unpacked into a plain dict.

```python
import asyncio

import vrchatapi
from vrchatapi.api import authentication_api
from vrchatapi.websocket import VRChatWebSocket


async def main():
    configuration = vrchatapi.Configuration(username="username", password="password")
    async with vrchatapi.ApiClient(configuration) as api_client:
        api_client.user_agent = "ExampleProgram/0.0.1 my@email.com"
        await authentication_api.AuthenticationApi(api_client).get_current_user()

        # Reads the auth cookie + User-Agent from the logged-in client.
        ws = VRChatWebSocket.from_client(api_client)

        @ws.on("friend-online")
        async def on_friend_online(event):
            print("online:", event.content["user"]["displayName"])

        # Or consume the same stream as an async iterator:
        #   async for event in ws:
        #       print(event.type, event.content)

        await ws.run()  # blocks; reconnects automatically by default
```

`VRChatWebSocket` supports callback registration (`ws.on("friend-online", ...)`
/ `@ws.on(...)`, a catch-all `ws.on_event(...)`), an async iterator over the
same event stream, error/connect/disconnect/reconnect hooks, automatic
reconnection with exponential backoff (`auto_reconnect=False` disables it), and
a configurable application-level heartbeat (default 30s;
`heartbeat_interval=None` disables it). See
[examples/examples-source/websocket.py](examples/examples-source/websocket.py)
and the [Websocket API reference](https://vrchat.community/websocket) for
details.

## High-level account API

`vrchatapi.highlevel` adds a dictionary-based API and a live account snapshot.
The existing generated model-based API remains unchanged. Responses retain
unknown fields, explicit nulls and missing fields, including partial updates.

```python
from vrchatapi.highlevel import VRChatAPI, VRChatAccount

api = VRChatAPI(
    {"username": "user", "password": "password"},
    user_agent="MyApplication/1.0 contact@example.com",
)
# get_current_user and verify2_fa / verify2_fa_email_code can also be used
# separately for interactive authentication. Persist api.cookie in your app.
current_user = await api.get_current_user()
account = VRChatAccount(
    api,
    current_user["id"],
    on_user=lambda user, world_changed: print(user.id, user.data),
    on_remove=lambda user_id: print("Removed", user_id),
    on_available=lambda available: print("Connected", available),
)
try:
    await account.start(current_user)
    # Keep your application's event loop running while using account.users.
finally:
    await account.close()
```

For interactive login, catch `vrchatapi.highlevel.TwoFactorAuthRequired` and
branch on its `challenge`: `TwoFactorAuthChallenge.EMAIL_OTP` uses
`verify2_fa_email_code`, while `TwoFactorAuthChallenge.TOTP` uses `verify2_fa`.
Then call `get_current_user` again. Classification uses the response's
`requiresTwoFactorAuth` field, independent of exception wording. The exception
is also an `UnauthorizedException`; unsupported challenges remain ordinary
`UnauthorizedException` errors.

The account owns its REST client, pipeline and default world cache. It fetches
friend pages, resolves missing users, applies pipeline changes in receive order,
and refreshes authentication and snapshots after disconnection. Authentication
failures are exposed through `on_auth_error`; initial setup errors are raised.
`on_authenticated` is an optional async callback for saving `api.cookie`.
Other callbacks are synchronous and must not block the event loop.

Each account has its own world cache by default. For deliberate sharing, pass
an explicit `WorldCache(fetch_world)` to multiple accounts and close it after
all consumers stop. A caller-supplied cache is never closed by an account.

`WorldCache.sorted_names` returns a cached, sorted tuple of unique names from
loaded worlds without fetching metadata. Update metadata with `cache.get(id, data)`
or assignment to `world.data`; in-place changes to the data dictionary or direct
mutation of `cache.registry` bypass name-cache invalidation. Name changes, cache
additions, pruning, and closure invalidate or clear the cached result.
World requests are deduplicated; cancelling one waiter does not cancel other
waiters. Closing the owner cancels pending fetches and retries.

The source of this API lives in `client/highlevel/`. `generate.sh` copies it to
`vrchatapi/highlevel/` after regeneration; edit the source, not the shipped copy.
`tools/stamp_version.py VERSION` stamps local release builds using the same
version step as generation. Release `1.21.0` includes this API.
    """,  # noqa: E501
    package_data={"vrchatapi": ["py.typed"]},
)
