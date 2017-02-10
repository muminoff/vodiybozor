# Helpers
from utils.helpers import format_text


async def process_menu_command(chat, match, logger):
    info = format_text('''
    *МЕНЮ*

    /ads - эълонлар
    /rules - канал қоидалари
    /contact - админлар билан боғланиш
    /stop - ботни тўхтатиш

    [Канал манзили](https://t.me/vodiybozor)
    ''')
    logger.info('%s menu requested by', chat.sender)
    await chat.send_text(info, parse_mode='Markdown', disable_web_page_preview=True)
