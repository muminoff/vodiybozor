import os
import logging
import textwrap
from aiotg import Bot

# Users
from queries.users import user_exists
from queries.users import insert_user
from queries.users import deactivate_user
from queries.users import has_user_products
from queries.users import is_user_admin


bot = Bot(
    api_token=os.environ.get('API_TOKEN'),
    name=os.environ.get('BOT_NAME'))

logger = logging.getLogger('bot')
logging.basicConfig(level=logging.DEBUG)

text = lambda t: textwrap.dedent(t)


@bot.command(r'/start')
async def start(chat, match):

    greeting = text('''
    Ассалому алайкум {name}!
    Водий бозорга хуш келибсиз.

    Бош менюга ўтиш учун /menu
    Маълумотлар /info
    Хизмат шартлари /eula
    Админ билан боғланиш /contact
    ''')

    await insert_user(chat.bot.pool, chat.sender)

    if await user_exists(chat.bot.pool, chat.sender):
        logger.info('User %s already exists', chat.sender)

    await chat.send_text(greeting.format(name=chat.sender['first_name']))

@bot.command(r'/menu')
def stop(chat, match):
    print(dir(chat))
    info = text('''
    Бош меню
    ''')
    logger.info('%s menu requested by', chat.sender)
    return chat.send_text(info)

@bot.command(r'/info')
def stop(chat, match):
    info = text('''
    Каналнинг қонун-қоидалари мавжуд ва админлар томонидан назорат қилинади.

    Қуйидаги хатти ҳаракатлар мумкин эмас:

    - бир кунда биттадан ортиқ эълон бериш;
    - бир эълонни қайта- қайта ёзиш;
    - эълонга алоқадор бўлмаган расм юклаш;
    - эълонга алоқаси йўқ хабарлар ёзиш;
    
    каналда қизиқарли ушлаб туриши учун эълонларни маълум вақт қўйилмасли,

    каналда эълонлар навбати бор

    Баъзи турдаги эълонларни қўймасликга канални хаққи бор

    Хизмат кўрсатиш эълонлари ёки такрорий эълонлар бўйича @musayev_i га мурожаат қилинг.
    ''')
    logger.info('%s info requested by', chat.sender)
    return chat.send_text(info)

@bot.command(r'/eula')
def stop(chat, match):
    info = text('''
    Хизмат шартлари
    ''')
    logger.info('%s eula requested by', chat.sender)
    return chat.send_text(info)

@bot.command(r'/contact')
def stop(chat, match):
    info = text('''
    Админ билан боғланиш
    ''')
    logger.info('%s contact requested by', chat.sender)
    return chat.send_text(info)

@bot.command(r'/stop')
async def stop(chat, match):
    farewell = text('''
    Қизиқиш учун раҳмат {name}.
    Каналимизни кузатишда давом этинг.
    Канал манзили https://t.me/vodiybozor
    ''')
    await deactivate_user(chat.bot.pool, chat.sender)
    logger.info('%s deactivated', chat.sender)
    await chat.send_text(farewell.format(name=chat.sender['first_name']), disable_web_page_preview=True)


@bot.command(r'/check')
async def check(chat, match):

    result = await has_user_products(chat.bot.pool, chat.sender)
    logger.info('User %s has products', result)

    await chat.send_text(result)


@bot.command(r'/amiadmin')
async def amiadmin(chat, match):

    result = await is_user_admin(chat.bot.pool, chat.sender)
    logger.info('User %s is admin', result)

    text = lambda r: 'admin' if r else 'not admin'

    await chat.send_text(text(result))
