import os
import asyncpg
import logging


logger = logging.getLogger('bot')


async def pool():
    dsn = os.environ.get('DATABASE_URL')
    return await asyncpg.create_pool(user='sardor', command_timeout=60)


async def sardor(sender):
    logger.info('Sender -> %s', sender)
    conn = await pool().acquire()

    try:
        values = await conn.fetch('''SELECT now()''')
        logger.info('Database query -> %s', values)
    finally:
        await pool.release(conn)
