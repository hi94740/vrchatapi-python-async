import asyncio

import vrchatapi
from vrchatapi.api import authentication_api
from vrchatapi.exceptions import UnauthorizedException
from vrchatapi.models.two_factor_auth_code import TwoFactorAuthCode
from vrchatapi.models.two_factor_email_code import TwoFactorEmailCode
from vrchatapi.websocket import VRChatWebSocket


async def main():
    configuration = vrchatapi.Configuration(
        username='username',
        password='password',
    )

    async with vrchatapi.ApiClient(configuration) as api_client:
        api_client.user_agent = "ExampleProgram/0.0.1 my@email.com"
        auth_api = authentication_api.AuthenticationApi(api_client)

        try:
            current_user = await auth_api.get_current_user()
        except UnauthorizedException as e:
            if e.status == 200:
                if "Email 2 Factor Authentication" in e.reason:
                    await auth_api.verify2_fa_email_code(
                        two_factor_email_code=TwoFactorEmailCode(input("Email 2FA Code: "))
                    )
                elif "2 Factor Authentication" in e.reason:
                    await auth_api.verify2_fa(
                        two_factor_auth_code=TwoFactorAuthCode(input("2FA Code: "))
                    )
                current_user = await auth_api.get_current_user()
            else:
                print("Exception when calling API: %s\n", e)
        except vrchatapi.ApiException as e:
            print("Exception when calling API: %s\n", e)

        print("Logged in as:", current_user.display_name)

        # The WebSocket (Pipeline) API pushes real-time updates: invites,
        # friend requests, friend online/offline events, group updates, ...
        # It needs the `auth` cookie and a proper User-Agent, both of which
        # are taken from the logged-in ApiClient.
        ws = VRChatWebSocket.from_client(api_client)

        @ws.on("friend-online")
        async def on_friend_online(event):
            user = event.content["user"]
            print(f"{user['displayName']} is now online in {user['location']}")

        @ws.on("notification")
        async def on_notification(event):
            print(f"New notification: {event.content['type']}")

        @ws.on_error
        async def on_error(exc):
            print("Pipeline error:", exc)

        # Blocks and reconnects automatically until the process is stopped.
        await ws.run()


if __name__ == "__main__":
    asyncio.run(main())
