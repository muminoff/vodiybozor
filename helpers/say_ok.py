# Helpers
from utils.helpers import format_text

# Misc
import random
import json

# Corpus
from corpus.ok import text as ok_text

async def attach_no_image_to_ad_command(chat, match, logger):
    answers = ('Яхши.', 'Дуруст.', 'Тушунарли.', 'ОК.')
    logger.info('%s says no image', chat.sender)
    await chat.send_text(text.format(ok=random.choice(answers)))
    await send_ad_acceptance_message(chat, match, logger)
