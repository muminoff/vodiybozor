import asyncio
import random
import sys


async def foo():
    while True:
        await asyncio.sleep(random.random())

async def bar():
    while True:
        await asyncio.sleep(random.random())


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()
