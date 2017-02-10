# Helpers
from utils.helpers import format_text


def process_menu_command(chat, match, logger):
    print(dir(chat))
    info = format_text('''
    Бош меню
    ''')
    logger.info('%s menu requested by', chat.sender)
    return chat.send_text(info)
