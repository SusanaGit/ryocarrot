import asyncio
from ryo_carrot_game import RyoCarrotGame

async def main():

    ryo_carrot_game_object = RyoCarrotGame()

    await ryo_carrot_game_object.main()

asyncio.run(main())