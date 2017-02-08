import asyncio
import uvloop
import os
from asyncpg import create_pool
from bot import bot

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def run_bot():
    await bot.loop()


async def make_pool():
    dsn = os.environ.get('DATABASE_URL')
    return await create_pool(dsn=dsn, min_size=10, max_size=20)


loop = asyncio.get_event_loop()
pool = loop.run_until_complete(make_pool())
setattr(bot, 'pool', pool)


if __name__ == '__main__':
    loop.run_until_complete(run_bot())
    # bot.run_webhook(webhook_url=os.environ.get('APP_URL') + 'webhook')
