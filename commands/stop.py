# Queries
from queries.users import deactivate_user

# Helpers
from utils.helpers import format_text


async def process_stop_command(chat, match, logger):
    farewell = format_text('''
    Қизиқиш учун раҳмат {name}.
    Каналимизни кузатишда давом этинг.
    Канал манзили https://t.me/vodiybozor
    ''')
    await deactivate_user(chat.bot.pg_pool, chat.sender)
    logger.info('%s deactivated', chat.sender)
    await chat.send_text(farewell.format(name=chat.sender['first_name']), disable_web_page_preview=True)
