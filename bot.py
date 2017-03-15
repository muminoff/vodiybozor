# Misc
import os
import logging

# Helpers
from utils.helpers import format_text

# Bot
from aiotg import Bot

from queries import user_has_any_draft
from queries import get_all_admins
from queries import user_is_admin

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

# Basic commands
from commands.basic import process_start_command
from commands.basic import process_menu_command
from commands.basic import process_rules_command
from commands.basic import process_stop_command
from commands.basic import process_unknown_command

# Ad related commands
from commands.ads import process_ads_command
from commands.ads import create_ad_command
from commands.ads import cancel_ad_command
from commands.ads import create_sale_ad_command
from commands.ads import create_sale_ad_vehicle_command
from commands.ads import create_sale_ad_vehicle_accept_command
from commands.ads import attach_image_to_ad_command
from commands.ads import attach_no_image_to_ad_command

# Photos
from commands.photos import process_photo, insert_watermark

# Contacts
from commands.contacts import process_contact

# Inline queries
from commands.inline import process_inline_query


@bot.command(r'/start')
@bot.command(r'/on')
async def start(chat, match):
    await process_start_command(chat, match, logger)
    await process_ads_command(chat, match, logger)


@bot.command(r'/ads')
async def ads(chat, match):
    await process_ads_command(chat, match, logger)


@bot.command(r'^(менюга|menyuga)\W*(қайтиш|qaytish)$')  # менюга қайтиш
@bot.command(r'/menu')
async def menu(chat, match):
    await process_menu_command(chat, match, logger)


@bot.command(r'/rules')
async def rules(chat, match):
    await process_rules_command(chat, match, logger)


@bot.default
async def unknown(chat, match):
    await process_unknown_command(chat, match, logger)


@bot.command(r'^(эълон|elon)\W*(бермоқчиман|bermoqchiman)$')
async def create_ad(chat, match):
    await create_ad_command(chat, match, logger)


@bot.command(r'^(эълонни|elonni)\W*(бекор|bekor)\W*(қилиш|qilish)$')
async def cancel_ad(chat, match):
    await cancel_ad_command(chat, match, logger)


@bot.command(r'^(сотмоқчиман|sotmoqchiman)$')
async def create_sale_ad(chat, match):
    await create_sale_ad_command(chat, match, logger)


@bot.command(r'\s*(авто|avto)\W*(ulov|улов)$')  # авто-улов
async def create_sale_ad_vehicle(chat, match):
    await create_sale_ad_vehicle_command(chat, match, logger)


@bot.command(r'\s*(авто|avto)\s*\:\s*([^,]+?)\s*\,\s*([^,]+?)\s*\,\s*([^,]+?)\s*\,\s*([^,]+?)\s*\,\s*([^,]+?)\s*\,\s*([^,]+?)?$')
@bot.command(r"\s*(avto|авто)\s*\:\s*(?P<name>[^,]+?)\s*\,\s*(?P<year>[^,]+?)\s*\,\s*(?P<mileage>[^,]+?)\s*\,\s*(?P<status>[^,]+?)\s*\,\s*(?P<price>[^,]+?)\s*\,\s*(?P<contact>[^,]+?)?$")
async def create_sale_ad_vehicle_accept(chat, match):
    await create_sale_ad_vehicle_accept_command(chat, match, logger)


@bot.command(r'\s*(rasm|расм)\W*(bor|бор)$')
async def attach_image_to_ad(chat, match):
    await attach_image_to_ad_command(chat, match, logger)


@bot.command(r'\s*(rasm|расм)\W*(yo\'q|yuq|йўқ|йук)$')
async def attach_no_image_to_ad(chat, match):
    await attach_no_image_to_ad_command(chat, match, logger)


@bot.inline
async def inline(iq):
    await process_inline_query(chat.bot.pg_pool, iq, logger)

@bot.command(r'/reklama')
async def make_self_ad(chat, match):
    ad_text = format_text('''
    🔱*Водий* *eBozor*🔱
    🇺🇿 *Автосалондаги* *нархлар* (2017 йил 25 февраль)
    🇷🇺 *Цены* *автомобилей* *в* *автосалоне* (за 25 февраля 2017 года)
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
    # await process_photo(chat, match, logger)
    url = await insert_watermark(chat, match, logger)
    await chat.send_photo(url)


@bot.handle("contact")
async def get_contact(chat, match):
    await process_contact(chat, match, logger)
