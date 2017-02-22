# Queries
from queries import insert_draft
from queries import user_has_draft
from queries import delete_draft
from queries import get_draft
from queries import get_all_admins

# Helpers
from utils.helpers import format_text

# Misc
import random
import json
import ast

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

    if await user_has_draft(chat.bot.pg_pool, chat.sender.get('id')):

        denied = format_text('''
        {name}, авто-улов ҳақида эълон бергандиз.
        У эълон ҳали каналга қўйилгани йўқ.

        У эълонни бекор қилайликми?
        ''')

        keyboard = [
            ['Эълонни бекор қилиш'],
            ['Менюга қайтиш'],
        ]
        reply_keyboard_markup = {
            'keyboard': keyboard,
            'resize_keyboard': True,
            'one_time_keyboard': True
        }

        await chat.send_text(
            denied.format(name=chat.sender['first_name']),
            parse_mode='Markdown',
            disable_web_page_preview=True,
            reply_markup=json.dumps(reply_keyboard_markup))
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


async def cancel_ad_command(chat, match, logger):

    if not await user_has_draft(chat.bot.pg_pool, chat.sender.get('id')):

        message = format_text('''
        {name}, ҳали янги эълон ёзганингиз йўқ.
        ''')
        await chat.send_text(
            message.format(name=chat.sender['first_name']),
            parse_mode='Markdown',
            disable_web_page_preview=True)
        return

    await delete_draft(chat.bot.pg_pool, chat.sender.get('id'))
    message = format_text('''
    Эълон бекор қилинди.
    ''')
    await chat.send_text(message)
    await create_sale_ad_vehicle_command(chat, match, logger)


async def create_sale_ad_vehicle_accept_command(chat, match, logger):
    logger.info('Vehicle create ad requested by %s', chat.sender)

    if await user_has_draft(chat.bot.pg_pool, chat.sender.get('id')):

        denied = format_text('''
        {name}, авто-улов ҳақида эълон бергандиз.
        У эълон ҳали каналга қўйилгани йўқ.

        У эълонни бекор қилайликми?
        ''')

        keyboard = [
            ['Эълонни бекор қилиш'],
            ['Менюга қайтиш'],
        ]
        reply_keyboard_markup = {
            'keyboard': keyboard,
            'resize_keyboard': True,
            'one_time_keyboard': True
        }

        await chat.send_text(
            denied.format(name=chat.sender['first_name']),
            parse_mode='Markdown',
            disable_web_page_preview=True,
            reply_markup=json.dumps(reply_keyboard_markup))
        return

    text = chat.message['text']
    keys = ['name', 'year', 'mileage', 'status', 'price', 'contact']
    __, values = text.split(':')
    values = [v.strip() for v in values.split(',')]
    ad_dict = dict(zip(keys, values))
    logger.info('----------------------')
    logger.info(ad_dict)
    logger.info('Inserting draft ...')
    await insert_draft(chat.bot.pg_pool, chat.sender['id'], ad_dict)
    ad_template = format_text('''
    🚗 *{name}* сотилади!
    ⚙️  *Йили:* {year}
    🏃 *Пробег:* {mileage}
    🔦 *Ҳолати:* {status}
    💰 *Нархи:* {price}
    📞 *Мурожаат учун:* /contact

    [Водий бозор](https://t.me/vodiybozor)
    ''')
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
    admins = await get_all_admins(chat.bot.pg_pool)

    import time
    start = time.time()

    # Make template
    ad_template = format_text('''
    🚗 *{name}* сотилади!
    ⚙️  *Йили:* {year}
    🏃 *Пробег:* {mileage}
    🔦 *Ҳолати:* {status}
    💰 *Нархи:* {price}
    📞 *Мурожаат учун:* {contact}

    [Водий бозор](https://t.me/vodiybozor)
    ''')
    draft = await get_draft(chat.bot.pg_pool, chat.sender.get('id'))
    logger.info('------- %s', type(draft))
    d = dict(draft)
    ad_str = d.get('data')
    ad_dict = ast.literal_eval(ad_str)
    ad_text = ad_template.format(**ad_dict)

    for admin in admins:
        logger.info('Sending to %s (%s)', admin['first_name'], admin['username'])

        private = chat.bot.private(admin['id'])
        try:
            await private.send_text(
                ad_text,
                parse_mode='Markdown',
                disable_web_page_preview=True)
        except:
            logger.info('Cannot send message to %s', admin['first_name'])
            pass

    logger.info('{0:0.4f} time spent to broadcast message to {1} admins'.format((time.time() - start), len(admins)))
    await send_ad_acceptance_message(chat, match, logger)

async def send_ad_acceptance_message(chat, match, logger):
    accepted_text = format_text('''
    Эълон қабул қилинди ва админларга юборилди.
    Тез орада каналга чоп этиб, бу ҳақда сизга хабар берамиз.
    ''')
    await chat.send_text(accepted_text)
