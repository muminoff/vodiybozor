# Asyncio
import asyncio

# UVLoop
import uvloop

# Asyncpg
from asyncpg import create_pool as create_pg_pool

# Aiobotocore
from aiobotocore import get_session as boto_session

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
        min_size=10,
        max_size=20)

async def make_s3_client(loop):
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    session = boto_session(loop=loop)
    return session.create_client(
        's3', region_name='us-east-1',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key)

# Main event loop
loop = asyncio.get_event_loop()

# Attach postgres connection pool to bot
pg_pool = loop.run_until_complete(make_pg_pool())
setattr(bot, 'pg_pool', pg_pool)

# Attach s3 client to bot
s3_client = loop.run_until_complete(make_s3_client(loop))
setattr(bot, 's3_client', s3_client)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == 'loop':
        loop.run_until_complete(run_bot())
    else:
        bot.run_webhook(os.environ.get('APP_URL') + 'webhook')
