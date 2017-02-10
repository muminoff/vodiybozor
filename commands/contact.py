# Queries
from queries.users import get_admins

# Helpers
from utils.helpers import format_text


async def process_contact_command(chat, match, logger):
    logger.info('%s contact requested by', chat.sender)

    contacts = format_text('''
    *Админлар:*

    {admins}
    ''')

    admins = []
    for admin in await get_admins(chat.bot.pg_pool):
        admins.append('@' + admin['username'])

    admins_text = '\n'.join(admins)
    await chat.send_text(contacts.format(admins=admins_text))
