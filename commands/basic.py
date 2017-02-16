# Queries
from queries import user_exists
from queries import insert_user
from queries import deactivate_user

# Helpers
from utils.helpers import format_text

# Misc
import json


async def process_start_command(chat, match, logger):
    has_last_name = lambda u: u.get('last_name', '') != ''
    first_name = chat.sender.get('first_name')
    fullname = first_name

    if has_last_name(chat.sender):
        fullname = first_name + ' ' + chat.sender.get('last_name')

    greeting = format_text('''
    Ассалому алайкум {name}!
    Водий бозорга хуш келибсиз.
    ''')

    await chat.send_chat_action('typing')
    await insert_user(chat.bot.pg_pool, chat.sender)

    if not await user_exists(chat.bot.pg_pool, chat.sender):
        logger.info('New user %s requested /start', chat.sender)
        await chat.send_text(greeting.format(name=fullname))


async def process_menu_command(chat, match, logger):
    info = format_text('''
    *МЕНЮ*

    /ads - эълонлар
    /subscribe - обуна
    /rules - канал қоидалари
    /contact - админлар билан боғланиш

    ''')
    logger.info('Menu requested by %s', chat.sender)
    await chat.send_chat_action('typing')
    await chat.send_text(info, parse_mode='Markdown', disable_web_page_preview=True)


async def process_rules_command(chat, match, logger):
    info = format_text('''
    *ХИЗМАТ* *ШАРТЛАРИ* *ВА* *ҚОИДАЛАР*

    1. Бир кунда бир тур бўйича биттадан ортиқ эълон бериш мумкин эмас.
    ''')
    logger.info('Rules requested by %s', chat.sender)
    await chat.send_chat_action('typing')
    await chat.send_text(info, parse_mode='Markdown', disable_web_page_preview=True)


async def process_contact_command(chat, match, logger):
    logger.info('Contact requested by %s', chat.sender)

    contacts = format_text('''
    *Админлар:*

    {admins}
    ''')

    admins = []
    for admin in await get_admins(chat.bot.pg_pool):
        admins.append('@' + admin)

    text = contacts.format(admins=admins).replace('\'', '')

    await chat.send_text(text, parse_mode='Markdown', disable_web_page_preview=True)


async def process_stop_command(chat, match, logger):
    farewell = format_text('''
    Қизиқиш учун раҳмат, {name}.
    [Каналимизни](https://t.me/vodiybozor) кузатишда давом этинг.
    ''')
    await deactivate_user(chat.bot.pg_pool, chat.sender)
    logger.info('%s deactivated', chat.sender)
    await chat.send_chat_action('typing')
    await chat.send_text(
        farewell.format(name=chat.sender['first_name']),
        parse_mode='Markdown',
        disable_web_page_preview=True)


async def process_unknown_command(chat, match, logger):
    question = format_text('''
    {name}, қизиқиш билдирганингиз учун раҳмат.

    Ҳозирда бу бўлим дастурлаштириляпти.
    ''')
    # question = format_text('''
    # {name}, мен ботман. Бунақа гапларни тўғриси тушунмайман. Мен фақат чой дамлайман холос. 😃

    # Балки, админларга бирор гапингиз бордир?
    # ''')
    keyboard = [
        [
            {
                'text': 'Телефон рақам юбориш',
                'request_contact': True
            }
        ]
        # ['👮🏻 дмин керак', '📃 Менюга қайтиш'],
    ]
    reply_keyboard_markup = {
        'keyboard': keyboard,
        'resize_keyboard': True,
        'one_time_keyboard': True
    }

    logger.info('Unknown requested by %s', chat.sender)
    await chat.send_chat_action('typing')
    await chat.send_text(
        question.format(name=chat.sender['first_name']),
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=json.dumps(reply_keyboard_markup))
