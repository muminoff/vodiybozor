import asyncio
import asyncpg


async def run():
    conn = await asyncpg.connect(user='sardor', password='', database='sardor', host='127.0.0.1')
    values = await conn.fetch('''SELECT now()''')
    print("------------>", values)
    await conn.close()

async def start():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
