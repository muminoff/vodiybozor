import asyncpg
import asyncio
import os



async def main():
    dsn = os.environ.get('DATABASE_URL')
    conn = await asyncpg.connect(dsn)
    q1 = asyncio.Queue()

    def listener(*args):
        q1.put_nowait(args)

    await conn.add_listener('test', listener)
    results = await conn.execute("NOTIFY test, 'qwerty'")
    print('---->', results)
    await conn.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
