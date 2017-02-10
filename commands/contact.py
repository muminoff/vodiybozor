# Helpers
from utils.helpers import format_text


def process_contact_command(chat, match, logger):
    info = format_text('''
    Админ билан боғланиш
    ''')
    logger.info('%s contact requested by', chat.sender)
    return chat.send_text(info)
