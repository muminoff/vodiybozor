# Misc
import os
import logging

# Helpers
from utils.helpers import format_text

# Bot
from aiotg import Bot

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
                            process_rules_command, process_contact_command,
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


@bot.command(r'/contact')
@bot.command(r'админ керак')
@bot.command(r'админ')
@bot.command(r'admin kerak')
@bot.command(r'admin')
async def contact(chat, match):
    await process_contact_command(chat, match, logger)


@bot.command(r'/stop')
async def stop(chat, match):
    await process_stop_command(chat, match, logger)


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


@bot.command(r'Эълонларни кўрмоқчиман')
@bot.command(r'elonlar')
async def view_ads(chat, match):
    info = format_text('''
    [Канал манзили](https://t.me/vodiybozor)
    ''')
    logger.info('View ads requested by %s', chat.sender)
    await chat.send_text(info, parse_mode='Markdown', disable_web_page_preview=True)

@bot.command(r'/reklama')
async def make_self_ad(chat, match):
    ad_text = format_text('''
    🔱*Водий* *eBozor*🔱

    🇺🇿 *Автосалондаги* *нархлар* (2017 йил 15 февраль)

    🇷🇺 *Цены* *автомобилей* *в* *автосалоне* (за 15 февраля 2017 года)

    ➥ [Nexia 3 Ravon(evro)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Isuzu -3](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Damas (1-2pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Matiz (1-4pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Matiz Best(1-3pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Spark Ravon(1-4pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Nexia-2 SOHC(1-4pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Nexia-2 DOHC(1-4pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Cobalt(1-4pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Gentra(1-4pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Orlando(1-3pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Captiva 3](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)
    ➥ [Malibu (1-3pozitsiya)](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)

    [➖➖➖➖➖➖➖➖➖➖➖](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q)

    👉 [Moshina narhlari 2017](https://telegram.me/joinchat/AAPpnD_lW9-Co3Erc8tR-Q) 👈 
    ''')
    await chat.send_text(ad_text, parse_mode='Markdown', disable_web_page_preview=True)


@bot.handle("photo")
async def get_photo(chat, match):
    await process_photo(chat, match, logger)


@bot.handle("contact")
async def get_contact(chat, match):
    await process_contact(chat, match, logger)
