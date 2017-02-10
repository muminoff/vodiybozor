# Helpers
from utils.helpers import format_text

# json
import json


async def process_unknown_command(chat, match, logger):
    question = format_text('''
    {name}, мен ботман. Бунақа гапларни тўғриси тушунмайман. Мен фақат чой дамлайман холос. 😃

    Балки, админларга бирор гапингиз бордир?
    ''')
    keyboard = [
        ['Админ керак', 'Менюни кўрмоқчиман'],
    ]
    reply_keyboard_markup = {
        'keyboard': keyboard,
        'resize_keyboard': True,
        'one_time_keyboard': True
    }

    logger.info('%s unknown requested by', chat.sender)
    await chat.send_text(
        question.format(name=chat.sender['first_name']),
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=json.dumps(reply_keyboard_markup))
