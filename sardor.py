from aiohttp import web

async def index(request):
    return web.Response(text="Welcome home!")

app = web.Application()
app.router.add_get('/', index)
