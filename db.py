import asyncio
import asyncpg
import os
import logging


async def run():
    logger = logging.getLogger('db')
    connection_dsn = os.environ.get('DATABASE_URL')
    conn = await asyncpg.connect(connection_dsn)
    values = await conn.fetch('''SELECT now()''')
    logger.info('Database query -> %s', values)
    await conn.close()

async def start():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
