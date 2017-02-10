# Helpers
from utils.helpers import format_text


def process_ads_command(chat, match, logger):
    info = format_text('''
    {name}, қайси бўлимдаги эълонларни кўрмоқчисиз?
    ''')
    logger.info('%s ads requested by', chat.sender)
    return chat.send_text(
            info.format(name=chat.sender['first_name']),
            parse_mode='Markdown',
            disable_web_page_preview=True)
