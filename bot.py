import os
import logging

from aiotg import Bot
import asyncpg

greeting = """
Ассалому алайкум, {name}!
Водий бозорга хуш келибсиз.
"""

help = """
Водий бозор канали учун махсус бот.

Ботдан фойдаланиш тартиби:
/publish - эълон ёзиш
/all - элонларни кўриш
/help - ёрдам бўлими
/contact - админ билан боғланиш
"""

not_found = """
Сўровингиз бўйича ҳеч қандай маълумот топилмади.
"""


bot = Bot(
        api_token=os.environ.get("API_TOKEN", "319964417:AAHAMcSBxtXJJzSwx1Lhyu1h6maLvIkfiCA"),
    name=os.environ.get("BOT_NAME", "VodiyBozorTestBot")
)
logger = logging.getLogger("bot")


@bot.command(r'/start')
async def start(chat, match):
    # tuid = chat.sender["id"]
    # if not (await db.users.find_one({ "id": tuid })):
    #     logger.info("new user %s", chat.sender)
    #     await db.users.insert(chat.sender.copy())
    # conn = await asyncpg.connect(user='sardor', password='', database='sardor', host='127.0.0.1')
    # values = await conn.prepare('''SELECT * FROM users''')
    # logger.info("values %s", values)
    # await conn.close()
    # async for value in values.cursor:
    #     await chat.send_text(value)
    logger.info("/start from %s", chat.sender)
    await chat.send_text(greeting.format(name=chat.sender['first_name']))


@bot.command(r'/stop')
async def stop(chat, match):
    # tuid = chat.sender["id"]
    logger.info("%s quit", chat.sender)
    await chat.send_text("Goodbye! We will miss you 😢")


@bot.command(r'/?help')
def usage(chat, match):
    return chat.send_text(help)
