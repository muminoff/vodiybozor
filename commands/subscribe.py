# Helpers
from utils.helpers import format_text


async def process_subscribe_command(chat, match, logger):
    info = format_text('''
    {name}, эълонларга обуна бўлмоқчимисиз ёки обуналарни кўрасизми?
    ''')
    keyboard = [
        ['Обуна бўлмоқчиман', 'Обуналарни кўрмоқчиман'],
        ['Менюга қайтиш'],
    ]
    reply_keyboard_markup = {
        'keyboard': keyboard,
        'resize_keyboard': True,
        'one_time_keyboard': True
    }

    logger.info('Subcscribe requested by %s', chat.sender)
    await chat.send_text(
        info.format(name=chat.sender['first_name']),
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=json.dumps(reply_keyboard_markup))
