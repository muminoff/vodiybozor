# Misc
import os
import logging

# Helpers
from utils.helpers import format_text

# Bot
from aiotg import Bot

from queries import user_has_any_draft
from queries import get_all_users

# Variables
api_token = os.environ.get('API_TOKEN')
bot_name = os.environ.get('BOT_NAME')

# Bot
bot = Bot(api_token=api_token, name=bot_name)

# Channel
channel = bot.channel(os.environ.get('CHANNEL_NAME', '@VodiyBozorTest'))

# Logging
logger = logging.getLogger('bot')
logging.basicConfig(level=logging.DEBUG)

# Commands
from commands.basic import (process_start_command, process_menu_command,
                            process_rules_command,
                            process_stop_command, process_unknown_command)
from commands.ads import (process_ads_command, create_ad_command,
                          create_sale_ad_command, create_sale_ad_vehicle_command,
                          create_sale_ad_vehicle_accept_command)

from commands.subscribe import process_subscribe_command

from commands.ads import (attach_image_to_ad_command,
                          attach_no_image_to_ad_command)

from commands.photos import process_photo
from commands.contacts import process_contact


@bot.command(r'салом')
@bot.command(r'salom')
@bot.command(r'/start')
async def start(chat, match):
    await process_start_command(chat, match, logger)
    await process_ads_command(chat, match, logger)


@bot.command(r'/ads')
async def ads(chat, match):
    await process_ads_command(chat, match, logger)


@bot.command(r'/subscribe')
async def subscribe(chat, match):
    await process_subscribe_command(chat, match, logger)


@bot.command(r'Менюга қайтиш')
@bot.command(r'Меню')
@bot.command(r'menu')
@bot.command(r'menyu')
@bot.command(r'Menyuga qaytish')
@bot.command(r'/menu')
async def menu(chat, match):
    await process_menu_command(chat, match, logger)


@bot.command(r'/rules')
async def rules(chat, match):
    await process_rules_command(chat, match, logger)


@bot.default
async def unknown(chat, match):
    await process_unknown_command(chat, match, logger)


@bot.command(r'Эълон бермоқчиман')
@bot.command(r'elon beraman')
@bot.command(r'elon bermoqchiman')
async def create_ad(chat, match):
    await create_ad_command(chat, match, logger)


@bot.command(r'сотаман')
@bot.command(r'сотмоқчиман')
@bot.command(r'sotaman')
@bot.command(r'sotmoqchiman')
async def create_sale_ad(chat, match):
    await create_sale_ad_command(chat, match, logger)


@bot.command(r'🚗 Авто-улов')
@bot.command(r'Авто-улов')
async def create_sale_ad_vehicle(chat, match):
    await create_sale_ad_vehicle_command(chat, match, logger)


@bot.command(r'Авто: (,\s*\d+)*')
async def create_sale_ad_vehicle_accept(chat, match):
    await create_sale_ad_vehicle_accept_command(chat, match, logger)


@bot.command(r'✅ Расм бор')
async def attach_image_to_ad(chat, match):
    await attach_image_to_ad_command(chat, match, logger)


@bot.command(r'❌ Расм йўқ')
async def attach_no_image_to_ad(chat, match):
    await attach_no_image_to_ad_command(chat, match, logger)


@bot.inline
async def inline(iq):
    logger.info('%s searching for %s', iq.sender, iq.query)
    message = {
        "message_text": "test content",
        "parse_mode": "markdown",
        "disable_web_page_preview": True
    }
    results = [
        {
            "type": "article",
            "id": str(x),
            "title": "test title " + str(x),
            "input_message_content": message,
            "description": "test description",
            "hide_url": True
        } for x in range(10)
    ]
    await iq.answer(results)


@bot.command(r'Эълонларни кўрмоқчиман')
@bot.command(r'elonlar')
async def view_ads(chat, match):
    info = format_text('''
    [Канал манзили](https://t.me/vodiybozor)
    ''')
    logger.info('View ads requested by %s', chat.sender)
    await chat.send_text(info, parse_mode='Markdown', disable_web_page_preview=True)


@bot.handle("photo")
async def get_photo(chat, match):
    file_id = chat.message['photo'][1]['file_id']
    logger.info('-------------')
    logger.info(chat.message['photo'])
    # await chat.send_photo(file_id)

    # if not await user_has_any_draft(chat.bot.pg_pool, chat.sender.get('id')):
    #     info = format_text('''
    #     {name}, расм юборишдан аввал эълон ёзишингиз керак.
    #     ''')
    #     logger.info('%s user sent photo with no draft', chat.sender)
    #     await chat.send_text(
    #         info.format(name=chat.sender['first_name']),
    #         parse_mode='Markdown',
    #         disable_web_page_preview=True)
    #     await create_sale_ad_command(chat, match, logger)
    #     return

    # category_id = await get_draft_category(chat.bot.pg_pool, chat.sender.get('id'))
    # draft = await get_draft(chat.bot.pg_pool, chat.sender.get('id'), category_id)
    # ad = await make_ad_from_draft(draft)
    url = await process_photo(chat, match, logger)
    await chat.send_photo(url, caption='test photo')


@bot.handle("contact")
async def get_contact(chat, match):
    await process_contact(chat, match, logger)


@bot.command(r'/boshla')
async def broadcast(chat, match):
    users = await get_all_users(chat.bot.pg_pool)

    for user in users:
        logger.info('Sending to %s (%s)', user['first_name'], user['username'])
        # text = format_text('''
        # Яна бир бор ассалому алайкум, {name}.

        # Яқин кунларда ишга тушаман. Шунга ўзим бир текшириб кўрмоқчидим. 😊
        # ''')
        text = '{name} test'
        ch = chat.bot.private(user['id'])
        try:
            await ch.send_text(text.format(name=user['first_name']))
        except:
            logger.info('Cannot send to %s', user)
            continue
