import logging
import os
import asyncio
import uvloop
from bot import bot


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def start():
    await bot.loop()


if __name__ == '__main__':
    loglevel = logging.DEBUG if os.getenv('DEBUG') else logging.INFO
    logging.basicConfig(level=loglevel)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        pass
