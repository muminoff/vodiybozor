# Asyncio
import asyncio

# UVLoop
import uvloop

# Asyncpg
from asyncpg import create_pool as create_pg_pool

# Aioredis
from aioredis import create_pool as create_redis_pool

# Bot
from bot import bot

# Misc
import os
from urllib.parse import urlparse

# Use uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def run_bot():
    await bot.loop()


async def make_pg_pool():
    dsn = os.environ.get('DATABASE_URL')
    return await create_pg_pool(
            dsn=dsn,
            min_size=1,
            max_size=2)


async def make_redis_pool():
    redis_url = os.environ.get('REDIS_URL')
    url = urlparse(redis_url)
    return await create_redis_pool(
            (url.hostname, url.port),
            password=url.password,
            minsize=1,
            maxsize=2)

# Main event loop
loop = asyncio.get_event_loop()

# Postgres connection pool
pg_pool = loop.run_until_complete(make_pg_pool())
setattr(bot, 'pg_pool', pg_pool)

redis_pool = loop.run_until_complete(make_redis_pool())
setattr(bot, 'redis_pool', redis_pool)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == 'loop':
        loop.run_until_complete(run_bot())
    else:
        bot.run_webhook(os.environ.get('APP_URL') + 'webhook')
