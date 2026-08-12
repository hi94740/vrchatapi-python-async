import asyncio

import vrchatapi
from vrchatapi.api.worlds_api import WorldsApi


async def main():
    # We don't add a configuration file/set a username and password
    async with vrchatapi.ApiClient() as api_client:
        api_client.user_agent = "ExampleProgram/0.0.1 my@email.com"

        # We don't use the authentication API at all, since we don't need to
        world_api = WorldsApi(api_client)
        world = await world_api.get_world("wrld_000000000-0000-0000-0000-000000000000")

        print(f"World `{world.name}` was made by `{world.author_name}` ({world.author_id})")


if __name__ == "__main__":
    asyncio.run(main())
