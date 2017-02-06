import asyncpg
import asyncio
import os


async def run():
    conn = await asyncpg.connect(user='sardor')
    stmt = await conn.prepare('SELECT id FROM users WHERE id = $1')
    print('user ->', await stmt.fetchval(56781796))
    await conn.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(run())
