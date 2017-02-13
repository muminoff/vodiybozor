async def process_contact(chat, match, logger):
    logger.info("Getting contact from %s", chat.sender)
    logger.info(chat.message['contact'])
    return
