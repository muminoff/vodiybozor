import os
from aiotg import Bot
import uvloop
import asyncio
import logging

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

bot = Bot(api_token=os.environ["API_TOKEN"])
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@bot.command(r"/echo (.+)")
def echo(chat, match):
    logger.info('%s', match.group())
    return chat.reply(match.group(1))


bot.run_webhook(webhook_url='https://aiotg.localtunnel.me')
