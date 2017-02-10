# Queries
from queries.users import user_exists
from queries.users import insert_user

# Helpers
from utils.helpers import format_text


async def process_start_command(chat, match, logger):
    greeting = format_text('''
    Ассалому алайкум {name}!
    Водий бозорга хуш келибсиз.

    Бош менюга ўтиш учун /menu
    Маълумотлар /info
    Хизмат шартлари /eula
    Админ билан боғланиш /contact
    ''')

    await insert_user(chat.bot.pg_pool, chat.sender)

    if await user_exists(chat.bot.pg_pool, chat.sender):
        logger.info('User %s already exists', chat.sender)

    await chat.send_text(greeting.format(name=chat.sender['first_name']))
