# Helpers
from utils.helpers import format_text


async def process_rules_command(chat, match, logger):
    info = format_text('''
    Хизмат шартлари
    ''')
    logger.info('%s eula requested by', chat.sender)
    await chat.send_text(info)
