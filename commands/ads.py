# Queries
from queries import insert_draft, user_has_draft

# Helpers
from utils.helpers import format_text

# Misc
import random
import json

# Corpus
from corpus.ok import text as ok_text


async def process_ads_command(chat, match, logger):
    info = format_text('''
    {name}, эълон бермоқчимисиз ёки эълонларни кўрмоқчимисиз?
    ''')
    keyboard = [
        ['Эълон бермоқчиман', 'Эълонларни кўрмоқчиман'],
        ['Менюга қайтиш'],
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
    {ok} Қандай эълон бермоқчисиз?
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
        question.format(ok=random.choice(ok_text)),
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

    if await user_has_draft(chat.bot.pg_pool, 1, chat.sender.get('id')):

        # with await chat.bot.redis_pool as conn:
        #     key = '{0}:{1}'.format(
        #         chat.sender['id'], '9a67d4d9-b283-4a30-9d84-904f66cb2a56')
        #     if await conn.exists(key):
        #         denied = format_text('''
        #         {name}, авто-улов ҳақида эълон бергандиз.
        #         У эълон ҳали каналга қўйилгани йўқ.

        #         У эълонни бекор қилайликми?
        #         ''')

        #         keyboard = [
        #             ['Эълонни бекор қилиш'],
        #             ['Менюга қайтиш'],
        #         ]
        #         reply_keyboard_markup = {
        #             'keyboard': keyboard,
        #             'resize_keyboard': True,
        #             'one_time_keyboard': True
        #         }

        #         await chat.send_text(
        #             denied.format(name=chat.sender['first_name']),
        #             parse_mode='Markdown',
        #             disable_web_page_preview=True,
        #             reply_markup=json.dumps(reply_keyboard_markup))
        #         return

        await chat.send_text(
            format_text('''
            You have draft in this category, delete or wait approval.
            '''),
            parse_mode='Markdown',
            disable_web_page_preview=True)
        return

    question = format_text('''
    Авто-улов ҳақида қисқа маълумот беринг.
    
    Эълонни бундай форматда вергул билан ажратиб ёзинг:
    ```
    Авто: Номи, йили, пробег, ҳолати, нархи, телефон рақам
    ```
    Масалан:
    ```
    Авто: Lacetti, 2015, 35000, яхши, 7000, +998931234567
    ```

    Бошига `Авто:` сўзини қўшиш эсдан чиқмасин.
    ''')

    logger.info('Vehicle create ad requested by %s', chat.sender)
    await chat.send_text(
        question,
        parse_mode='Markdown',
        disable_web_page_preview=True)


async def create_sale_ad_vehicle_accept_command(chat, match, logger):
    logger.info('Vehicle create ad requested by %s', chat.sender)

    ad_template = format_text('''
    🚗 *{name}* сотилади!
    ⚙️  *Йили:* {year}
    🏃 *Пробег:* {mileage}
    🔦 *Ҳолати:* {status}
    💰 *Нархи:* {price}
    📞 *Мурожаат учун:* /contact

    [Водий бозор](https://t.me/vodiybozor)
    ''')

    text = chat.message['text']
    keys = ['name', 'year', 'mileage', 'status', 'price', 'contact']
    __, values = text.split(':')
    values = [v.strip() for v in values.split(',')]
    ad_dict = dict(zip(keys, values))
    logger.info('----------------------')
    logger.info(ad_dict)
    logger.info('Inserting draft ...')
    await insert_draft(chat.bot.pg_pool, 1, chat.sender['id'], ad_dict)
    ad_text = ad_template.format(**ad_dict)
    await chat.send_text(
        ad_text,
        parse_mode='Markdown',
        disable_web_page_preview=True)

    question = format_text('''
    Эълон ёзиб олинди.

    Расми борми йўқми?
    ''')
    keyboard = [
        ['✅ Расм бор', '❌ Расм йўқ'],
    ]
    reply_keyboard_markup = {
        'keyboard': keyboard,
        'resize_keyboard': True,
        'one_time_keyboard': True
    }

    logger.info('Vehicle ad accepted from %s', chat.sender)
    await chat.send_text(
        question,
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=json.dumps(reply_keyboard_markup))


async def attach_image_to_ad_command(chat, match, logger):
    ask_image = format_text('''
    Юборинг расмни.
    ''')
    logger.info('Image file sent by %s', chat.sender)
    await chat.send_text(ask_image)


async def attach_no_image_to_ad_command(chat, match, logger):
    text = format_text('''
    {ok}
    ''')
    logger.info('%s says no image', chat.sender)
    await chat.send_text(text.format(ok=random.choice(ok_text)))
    await send_ad_acceptance_message(chat, match, logger)

async def send_ad_acceptance_message(chat, match, logger):
    accepted_text = format_text('''
    Эълон қабул қилинди ва админларга юборилди.
    Тез орада каналга чоп этиб, бу ҳақда сизга хабар берамиз.
    ''')
    await chat.send_text(accepted_text)
