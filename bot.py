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

# Contacts
from commands.contacts import process_contact

# Inline queries
from commands.inline import process_inline_query


@bot.command(r'/start')
async def start(chat, match):
    await process_start_command(chat, match, logger)
    await process_ads_command(chat, match, logger)


@bot.command(r'/ads')
async def ads(chat, match):
    await process_ads_command(chat, match, logger)


@bot.command(r'/menu')
async def menu(chat, match):
    await process_menu_command(chat, match, logger)


@bot.command(r'/rules')
async def rules(chat, match):
    await process_rules_command(chat, match, logger)


@bot.default
async def unknown(chat, match):
    await process_unknown_command(chat, match, logger)


@bot.command(r'эълон бермоқчиман')
async def create_ad(chat, match):
    await create_ad_command(chat, match, logger)


@bot.command(r'эълонни бекор қилиш')
async def cancel_ad(chat, match):
    await cancel_ad_command(chat, match, logger)


@bot.command(r'сотмоқчиман')
async def create_sale_ad(chat, match):
    await create_sale_ad_command(chat, match, logger)


@bot.command(r'🚗 авто-улов')
async def create_sale_ad_vehicle(chat, match):
    await create_sale_ad_vehicle_command(chat, match, logger)


@bot.command(r'авто: (,\s*\d+)*')
async def create_sale_ad_vehicle_accept(chat, match):
    await create_sale_ad_vehicle_accept_command(chat, match, logger)


@bot.command(r'✅ расм бор')
async def attach_image_to_ad(chat, match):
    await attach_image_to_ad_command(chat, match, logger)


@bot.command(r'❌ расм йўқ')
async def attach_no_image_to_ad(chat, match):
    await attach_no_image_to_ad_command(chat, match, logger)


@bot.inline
async def inline(iq):
    await process_inline_query(chat.bot.pg_pool, iq, logger)


@bot.handle("photo")
async def get_photo(chat, match):
    await process_photo(chat, match, logger)


@bot.handle("contact")
async def get_contact(chat, match):
    await process_contact(chat, match, logger)
