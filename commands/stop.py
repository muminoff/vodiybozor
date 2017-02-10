# Queries
from queries.users import deactivate_user

# Helpers
from utils.helpers import format_text


async def process_stop_command(chat, match, logger):
    farewell = format_text('''
    Қизиқиш учун раҳмат, {name}.
    [Каналимизни](https://t.me/vodiybozor) кузатишда давом этинг.
    ''')
    await deactivate_user(chat.bot.pg_pool, chat.sender)
    logger.info('%s deactivated', chat.sender)
    await chat.send_text(
            farewell.format(name=chat.sender['first_name']),
            parse_mode='Markdown',
            disable_web_page_preview=True)
