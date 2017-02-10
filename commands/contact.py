# Helpers
from utils.helpers import format_text


async def process_contact_command(chat, match, logger):
    info = format_text('''
    Админ билан боғланиш
    ''')
    logger.info('%s contact requested by', chat.sender)
    await chat.send_text(info)
