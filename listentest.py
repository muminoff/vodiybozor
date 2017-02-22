import asyncpg
import asyncio
import os
import random
import json
import string
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def producer():
    dsn = os.environ.get('DATABASE_URL')
    conn = await asyncpg.connect(dsn)

    while True:

        value = json.dumps({'foo': 'bar %f' % random.random()})
        
        await conn.execute("NOTIFY test, '%s'" % value)
        await asyncio.sleep(random.random() * random.random())

    await conn.close()

async def consumer(loop):
    dsn = os.environ.get('DATABASE_URL')
    conn = await asyncpg.connect(dsn)
    q = asyncio.Queue(loop=loop)

    def listener(*args):
        q.put_nowait(args)

    await conn.add_listener('test', listener)

    while True:
        result = await q.get()
        data = result[-1]
        logging.info('----------> %s', json.loads(data))

    await conn.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(producer())
    loop.create_task(consumer(loop))

    loop.run_forever()
    loop.close()
