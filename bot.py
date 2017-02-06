import os
import logging
from aiotg import Bot
import textwrap


bot = Bot(
    api_token=os.environ.get('API_TOKEN'),
    name=os.environ.get('BOT_NAME'))

logger = logging.getLogger('bot')
logging.basicConfig(level=logging.DEBUG)

text = lambda t: textwrap.dedent(t)


@bot.command(r'/start')
async def start(chat, match):

    first_time_greeting = text("""
    Ассалому алайкум {name}!
    Водий бозорга хуш келибсиз.
    """)

    greeting = text("""
    Нима хизмат бор {name}?
    """)

    id = chat.sender.get('id')
    first_name = chat.sender.get('first_name')
    last_name = chat.sender.get('last_name', '')
    username = chat.sender.get('username', '')

    async with chat.bot.pool.acquire() as conn:
        try:
            if not (await conn.fetch('SELECT id FROM users WHERE id=$1', chat.sender['id'])):
                logger.info('New user --> %s', chat.sender)
                await conn.execute('''
                INSERT INTO users(id, first_name, last_name, username)
                VALUES ($1, $2, $3, $4)
                ''', id, first_name, last_name, username)
                reply_text = first_time_greeting.format(name=first_name)
            else:
                reply_text = greeting.format(name=first_name)

            await chat.send_text(reply_text)

        finally:
            await chat.bot.pool.release(conn)
