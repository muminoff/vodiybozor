import os
import logging
import textwrap
from aiotg import Bot

# Users
from queries.users import user_exists
from queries.users import insert_user
from queries.users import deactivate_user


bot = Bot(
    api_token=os.environ.get('API_TOKEN'),
    name=os.environ.get('BOT_NAME'))

logger = logging.getLogger('bot')
logging.basicConfig(level=logging.DEBUG)

text = lambda t: textwrap.dedent(t)


@bot.command(r'/start')
async def start(chat, match):

    greeting = text('''
    Ассалому алайкум {name}!
    Водий бозорга хуш келибсиз.

    Бош менюга ўтиш учун /menu
    Маълумотлар /info
    Хизмат шартлари /eula
    Админ билан боғланиш /contact
    ''')

    await insert_user(chat.bot.pool, chat.sender)

    if await user_exists(chat.bot.pool, chat.sender):
        logger.info('User %s already exists', chat.sender)

    await chat.send_text(greeting.format(name=chat.sender['first_name']))

@bot.command(r'/stop')
async def stop(chat, match):
    farewell = text('''
    Қизиқиш ва эътибор учун раҳмат {name}.
    Каналимизни кузатишда давом этинг.
    Каналимиз манзили https://t.me/vodiybozor
    ''')
    await deactivate_user(chat.bot.pool, chat.sender)
    logger.info('%s deactivated', chat.sender)
    await chat.send_text(farewell.format(name=chat.sender['first_name']), disable_web_page_preview=True)
