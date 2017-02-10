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
                          create_sale_ad_command)


@bot.command(r'/start')
async def start(chat, match):
    await process_start_command(chat, match, logger)
    await process_ads_command(chat, match, logger)


@bot.command(r'/ads')
async def ads(chat, match):
    await process_ads_command(chat, match, logger)


@bot.command(r'Менюни кўрмоқчиман')
@bot.command(r'/menu')
async def menu(chat, match):
    await process_menu_command(chat, match, logger)


@bot.command(r'/rules')
async def rules(chat, match):
    await process_rules_command(chat, match, logger)


@bot.command(r'/contact')
@bot.command(r'Админ керак')
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
    test = format_text('''
    *СОТИЛАДИ*

    *Galaxy* *S5*
    *Нархи:* 300 y.e.
    *Ҳолати:* аъло

    📞 [Боғланиш](https://t.me/muminofff)
    ''')
    logger.info('%s unkknown requested by', chat.sender)
    await channel.send_text(test, parse_mode='Markdown', disable_web_page_preview=True)


@bot.command(r'elon bor')
@bot.command(r'elon bermoqchiman')
@bot.command(r'Эълон бермоқчиман')
async def create_ad(chat, match):
    await create_ad_command(chat, match, logger)


@bot.command(r'sotmoqchiman')
@bot.command(r'Сотмоқчиман')
async def create_ad(chat, match):
    await create_sale_ad_command(chat, match, logger)


@bot.command(r'Эълонларни кўрмоқчиман')
async def view_ads(chat, match):
    await chat.send_text(
        'view ads ok!',
        parse_mode='Markdown',
        disable_web_page_preview=True)
