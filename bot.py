import os
import logging

# Bot
from aiotg import Bot

# Commands
from commands.start import process_start_command
from commands.ads import process_ads_command
from commands.menu import process_menu_command
from commands.rules import process_rules_command
from commands.contact import process_contact_command
from commands.stop import process_stop_command
from commands.unknown import process_unknown_command

# Variables
api_token = os.environ.get('API_TOKEN')
bot_name = os.environ.get('BOT_NAME')

# Bot
bot = Bot(api_token=api_token, name=bot_name)

# Channel
channel = bot.channel(os.environ.get('CHANNEL_NAME', 'VodiyBozorTestChannel'))

# Logging
logger = logging.getLogger('bot')
logging.basicConfig(level=logging.DEBUG)


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


@bot.command(r'Админ керак')
@bot.command(r'/contact')
async def contact(chat, match):
    await process_contact_command(chat, match, logger)


@bot.command(r'/stop')
async def stop(chat, match):
    await process_stop_command(chat, match, logger)


@bot.default
async def unknown(chat, match):
    await process_unknown_command(chat, match, logger)
    await channel.send_text('test')


@bot.command(r'Эълон бермоқчиман')
async def create_ad(chat, match):
    await chat.send_text(
        'create ad ok!',
        parse_mode='Markdown',
        disable_web_page_preview=True)


@bot.command(r'Эълонларни кўрмоқчиман')
async def create_ad(chat, match):
    await chat.send_text(
        'view ads ok!',
        parse_mode='Markdown',
        disable_web_page_preview=True)


@bot.command(r'Менюни кўрмоқчиман')
async def create_ad(chat, match):
    await process_menu_command(chat, match, logger)
