# Queries
from queries.users import user_exists
from queries.users import insert_user
from queries.users import deactivate_user
from queries.users import get_admins

# Helpers
from utils.helpers import format_text

# Misc json


async def process_start_command(chat, match, logger):
    greeting = format_text('''
    Ассалому алайкум {name}!
    Водий бозорга хуш келибсиз.
    ''')

    await insert_user(chat.bot.pg_pool, chat.sender)

    if await user_exists(chat.bot.pg_pool, chat.sender):
        logger.info('User %s already exists', chat.sender)

    await chat.send_text(greeting.format(name=chat.sender['first_name']))


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


async def process_rules_command(chat, match, logger):
    info = format_text('''
    Хизмат шартлари
    ''')
    logger.info('%s eula requested by', chat.sender)
    await chat.send_text(info)


async def process_contact_command(chat, match, logger):
    logger.info('%s contact requested by', chat.sender)

    contacts = format_text('''
    *Админлар:*

    {admins}
    ''')

    admins = []
    for admin in await get_admins(chat.bot.pg_pool):
        admins.append('@' + admin['username'])

    admins_text = '\n'.join(admins)
    await chat.send_text(contacts.format(admins=admins_text), parse_mode='Markdown', disable_web_page_preview=True)


async def process_stop_command(chat, match, logger):
    farewell = format_text('''
    Қизиқиш учун раҳмат, {name}.
    [Каналимизни](https://t.me/vodiybozor) кузатишда давом этинг.
    ''')
    await deactivate_user(chat.bot.pg_pool, chat.sender)
    logger.info('%s deactivated', chat.sender)
    await chat.send_text(
        farewell.format(name=chat.sender['first_name']),
        parse_mode='Markdown',
        disable_web_page_preview=True)


async def process_unknown_command(chat, match, logger):
    question = format_text('''
    {name}, мен ботман. Бунақа гапларни тўғриси тушунмайман. Мен фақат чой дамлайман холос. 😃

    Балки, админларга бирор гапингиз бордир?
    ''')
    keyboard = [
        ['👮🏻 Админ керак', '📃 Менюни кўрмоқчиман'],
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
