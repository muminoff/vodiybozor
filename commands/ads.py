# Helpers
from utils.helpers import format_text

# json
import json


async def process_ads_command(chat, match, logger):
    info = format_text('''
    {name}, эълон бермоқчимисиз ёки эълонларни кўрмоқчимисиз?
    ''')
    keyboard = [
        ['Эълон бермоқчиман', 'Эълонларни кўрмоқчиман'],
        ['Менюни кўрмоқчиман'],
    ]
    reply_keyboard_markup = {
        'keyboard': keyboard,
        'resize_keyboard': True,
        'one_time_keyboard': True
    }

    logger.info('%s ads requested by', chat.sender)
    await chat.send_text(
        info.format(name=chat.sender['first_name']),
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=json.dumps(reply_keyboard_markup))


async def create_ad_command(chat, match, logger):
    question = format_text('''
    Жуда яхши. Қандай эълон бермоқчисиз?
    ''')
    keyboard = [
        ['Сотмоқчиман', 'Олмоқчиман'],
        ['Хизмат ва таклифлар'],
    ]
    reply_keyboard_markup = {
        'keyboard': keyboard,
        'resize_keyboard': True,
        'one_time_keyboard': True
    }

    logger.info('%s ads requested by', chat.sender)
    await chat.send_text(
        question,
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=json.dumps(reply_keyboard_markup))


async def create_sale_ad_command(chat, match, logger):
    question = format_text('''
    Нима сотмоқчисиз?
    ''')
    keyboard = [
        [':car: Авто-улов', ':house: Кўчмас-мулк'],
        [':tv: Маиший техника', ':door: Уй-рўзғор буюмлари'],
        [':shirt: Кийим-кечак', ':bicyclist: Спорт анжомлари'],
        [':iphone: Телефон', ''],
    ]
    reply_keyboard_markup = {
        'keyboard': keyboard,
        'resize_keyboard': True,
        'one_time_keyboard': True
    }

    logger.info('%s ads requested by', chat.sender)
    await chat.send_text(
        question,
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=json.dumps(reply_keyboard_markup))
