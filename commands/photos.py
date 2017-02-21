# Urllib
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

# Download file
from aiohttp import web
from pathlib import PurePath

# Helpers
from utils.helpers import format_text

# Wand
from wand.image import Image
from wand.display import display

# Queries
from queries import user_has_draft, get_draft, get_all_admins

# Commands
from commands.ads import create_sale_ad_command

# Misc
import os
import ast


async def process_photo(chat, match, logger):
    logger.info("Getting photo from %s", chat.sender)
    file_id = chat.message['photo'][1]['file_id']

    if await user_has_draft(chat.bot.pg_pool, chat.sender.get('id')):
        info = format_text('''
        {name}, расм юборишдан аввал эълон ёзишингиз керак.
        ''')
        logger.info('%s user sent photo with no draft', chat.sender)
        await chat.send_text(
            info.format(name=chat.sender['first_name']),
            parse_mode='Markdown',
            disable_web_page_preview=True)
        await create_sale_ad_command(chat, match, logger)
        return

    admins = await get_all_admins(chat.bot.pg_pool)

    import time
    start = time.time()
    # Make template
    ad_template = format_text('''
    🚗 {name} сотилади!
    ⚙️  Йили: {year}
    🏃 Пробег: {mileage}
    🔦 Ҳолати: {status}
    💰 Нархи: {price}
    📞 Мурожаат: {contact}
    ''')
    draft = await get_draft(chat.bot.pg_pool, chat.sender.get('id'))
    d = dict(draft)
    ad_str = d.get('data')
    ad_dict = ast.literal_eval(ad_str)
    ad_text = ad_template.format(**ad_dict)

    for admin in admins:
        logger.info('Sending to %s (%s)', admin['first_name'], admin['username'])

        private = chat.bot.private(admin['id'])
        try:
            await private.send_photo(url, caption=ad_text)
        except:
            logger.info('Cannot send photo to %s', admin['first_name'])
            pass

    logger.info('{0:0.4f} time spent to broadcast message to {1} admins'.format((time.time() - start), len(admins)))
    await send_ad_acceptance_message(chat, match, logger)
    url = await insert_watermark(chat, match, logger)


async def insert_watermark(chat, match, logger):
    file_id = chat.message['photo'][-1]['file_id']

    chunk_size = 8192
    file = await chat.bot.get_file(file_id)
    file_path = file["file_path"]
    p = PurePath(file_path)
    new_filename = '{0}{1}'.format(file_id, p.suffix)

    async with chat.bot.download_file(file_path) as r:
        bg_url = r.url
        fg_url = 'http://imgur.com/download/CrGVjV6'

        bg = urllib2.urlopen(bg_url)
        with Image(file=bg) as bg_img:
            fg = urllib2.urlopen(fg_url)
            with Image(file=fg) as fg_img:
                bg_img.composite(
                    fg_img,
                    left=int((bg_img.width - fg_img.width) / 2),
                    top=int((bg_img.height - fg_img.height) - (fg_img.height / 2)))
                bg_img.save(filename=new_filename)
            fg.close()
        bg.close()

        with open(new_filename, 'rb') as data:
            bucket = 'vodiybozor'
            await chat.bot.s3_client.put_object(Bucket=bucket, Key=new_filename, Body=data)

    url = 'https://s3.amazonaws.com/vodiybozor/{0}'.format(new_filename)
    os.remove(new_filename)
    return url
