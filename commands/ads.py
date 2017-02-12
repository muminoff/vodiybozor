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
        ['🚗 Авто-улов', '🏠 Кўчмас-мулк'],
        ['📺 Маиший техника', '🚪 Уй-рўзғор буюмлари'],
        ['👕 Кийим-кечак', '🚴 Спорт анжомлари'],
        ['📱 Телефон', ''],
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


async def create_sale_ad_vehicle_command(chat, match, logger):
    question = format_text('''
    Авто-улов ҳақида қисқа ва лўнда маълумот беринг.
    
    Эълон бундай форматда қабул қилинади, вергул билан ажратиб ёзинг:
    ```
    Авто: Номи, йили, пробег, ҳолати, нархи, манзил, телефон рақам (ёки телеграм)
    ```
    Масалан:
    ```
    Авто: Lacetti, 2015, 35000, яхши, 7000, +998931234567
    ёки
    Авто: Nexia DOHC, 2009, 145000, яхши, 5000, Андижон, @foobar
    ```
    ''')

#     #Galaxy #Note 3 sotiladi
#     :m: Xolati yaxshi
#     :package:Коropka dakumenti bor
#     :moneybag:800.000 so'm
#     :phone:+998914898109
#     :triangular_flag_on_post:Andijon
#     Telegram:point_right: @Mamatxonov95

    logger.info('Vehicle create ad requested by %s', chat.sender)
    await chat.send_text(
        question,
        parse_mode='Markdown',
        disable_web_page_preview=True)


async def create_sale_ad_vehicle_accept_command(chat, match, logger, channel):
    logger.info('Vehicle create ad requested by %s', chat.sender)

    ad_template = format_text('''
    *{name}* сотилади!
    *Йили:* {year}
    *Пробег:* {mileage}
    *Ҳолати:* {status}
    *Нархи:* {price}
    *Манзил:* {location}
    *Боғланиш:* {contact}

    [Водий бозор](https://t.me/vodiybozor)
    ''')

    text = chat.message['text']
    keys = ['name', 'year', 'mileage', 'status', 'price', 'location', 'contact']
    __, values = text.split(':')
    values = values.strip(' ').split(',')
    ad_dict = dict(zip(keys, values))
    ad_text = ad_template.format(**ad_dict)

    await channel.send_text(
        ad_text,
        parse_mode='Markdown',
        disable_web_page_preview=True)
