# Main
from aiotg import Bot

# Misc
import os
import logging

# Database
from database import sardor

greeting = '''
Ассалому алайкум, {name}!
Водий бозорга хуш келибсиз.
'''

help = '''
Водий бозор канали учун махсус бот.

Ботдан фойдаланиш тартиби:
/publish - эълон ёзиш
/all - элонларни кўриш
/help - ёрдам бўлими
/contact - админ билан боғланиш
'''

not_found = '''
Сўровингиз бўйича ҳеч қандай маълумот топилмади.
'''


bot = Bot(
    api_token=os.environ.get('API_TOKEN'),
    name=os.environ.get('BOT_NAME')
)
logger = logging.getLogger('bot')


@bot.command(r'/start')
async def start(chat, match):
    await chat.send_text(greeting.format(name=chat.sender['first_name']))
    logger.info('/start from %s', chat.sender)


@bot.command(r'/?help')
def usage(chat, match):
    return chat.send_text(help)
