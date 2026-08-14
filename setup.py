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

    The version of the OpenAPI document: 1.20.8
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
VERSION = "1.20.9"
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
    """,  # noqa: E501
    package_data={"vrchatapi": ["py.typed"]},
)
