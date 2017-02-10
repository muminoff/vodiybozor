import os
import logging

# Bot
from aiotg import Bot

# Commands
from commands.start import process_start_command
from commands.menu import process_menu_command
from commands.rules import process_rules_command
from commands.contact import process_contact_command
from commands.stop import process_stop_command

# Users
from queries.users import deactivate_user
from queries.users import get_admins

# Variables
api_token = os.environ.get('API_TOKEN')
bot_name = os.environ.get('BOT_NAME')

# Bot
bot = Bot(api_token=api_token, name=bot_name)

# Logging
logger = logging.getLogger('bot')
logging.basicConfig(level=logging.DEBUG)


@bot.default
@bot.command(r'/start')
async def start(chat, match):
    await process_start_command(chat, match, logger)

@bot.command(r'/menu')
def menu(chat, match):
    return process_menu_command(chat, match, logger)

@bot.command(r'/rules')
def rules(chat, match):
    return process_rules_command(chat, match, logger)

@bot.command(r'/contact')
def contact(chat, match):
    process_contact_command(chat, match, logger)

@bot.command(r'/stop')
async def stop(chat, match):
    await process_stop_command(chat, match, logger)
