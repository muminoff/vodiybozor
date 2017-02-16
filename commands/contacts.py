# Helpers
from utils.helpers import format_text

# Queries
from queries import insert_contact


async def process_contact(chat, match, logger):
    logger.info("Getting contact from %s", chat.sender)
    logger.info(chat.message['contact'])
    if await insert_contact(chat.bot.pg_pool, chat.message['contact']):
        info = format_text('''
        Телефон рақам қабул қилинди. Раҳмат.
        ''')
        logger.info('Received contact from %s', chat.sender)
        await chat.send_text(info, parse_mode='Markdown', disable_web_page_preview=True)
