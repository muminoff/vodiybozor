import asyncio
import uvloop
import os
from asyncpg import create_pool
from bot import bot

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from aiohttp import web


async def make_pool():
    dsn = os.environ.get('DATABASE_URL')
    return await create_pool(dsn=dsn, min_size=1, max_size=2)


async def index(request):
    return web.Response(text="VodiyBozor")

app = web.Application()
app.router.add_route('GET', '/', index)
app.router.add_route('POST', '/webhook', bot.webhook_handle)
setattr(bot, 'pool', make_pool())


# async def run_bot():
#     await bot.loop()


# async def make_pool():
#     dsn = os.environ.get('DATABASE_URL')
#     return await create_pool(dsn=dsn, min_size=1, max_size=2)


# Main loop
# loop = asyncio.get_event_loop()

# # Make pool
# pool = loop.run_until_complete(make_pool())
# setattr(bot, 'pool', pool)

# App
# app = bot.create_webhook_app('/webhook')


# if __name__ == '__main__':
#     # loop.run_until_complete(run_bot())
#     bot.run_webhook(webhook_url=os.environ.get('APP_URL') + 'webhook')

