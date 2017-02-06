import logging
from aiotg import Bot
import os
import asyncio
import uvloop
from asyncpg import create_pool

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# Main

greeting = '''
Hi {name}!
'''

help = '''
Help menu
'''

not_found = '''
Not found
'''


bot = Bot(
    api_token=os.environ.get('API_TOKEN'),
    name=os.environ.get('BOT_NAME'))

logger = logging.getLogger('bot')
loglevel = logging.DEBUG
logging.basicConfig(level=loglevel)


@bot.command(r'/start')
async def start(chat, match):
    await chat.send_text(greeting.format(name=chat.sender['first_name']))
    logger.info('/start from %s', chat.sender)

    async with pool.acquire() as connection:
        try:
            if not (await connection.fetch('SELECT id FROM users WHERE id=$1', chat.sender['id'])):
                id = chat.sender.get('id')
                first_name = chat.sender.get('first_name')
                last_name = chat.sender.get('last_name', '')
                username = chat.sender.get('username', '')
                logger.info('New user --> %s', chat.sender)
                await connection.execute('''
                INSERT INTO users(id, first_name, last_name, username)
                VALUES ($1, $2, $3, $4)
                ''', id, first_name, last_name, username)

            values = await connection.fetch('SELECT now()')
            await chat.send_text(values)
        finally:
            await pool.release(connection)


@bot.command(r'/?help')
def usage(chat, match):
    return chat.send_text(help)


async def run_bot():
    await bot.loop()

async def make_pool():
    dsn = os.environ.get('DATABASE_URL')
    return await create_pool(dsn, max_size=20)


loop = asyncio.get_event_loop()
pool = loop.run_until_complete(make_pool())


if __name__ == '__main__':
    loop.run_until_complete(run_bot())
