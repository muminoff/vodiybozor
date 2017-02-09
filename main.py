from aiohttp import web
from bot import bot


async def index(request):
    return web.Response(text="VodiyBozor")


app = web.Application()
app.router.add_route('GET', '/', index)
app.router.add_route('POST', '/webhook', bot.webhook_handle)
