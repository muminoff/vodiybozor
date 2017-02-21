async def process_inline_query(pg_pool, iq, logger):
    logger.info('%s searching for %s', iq.sender, iq.query)
    message = {
        "message_text": "test content",
        "parse_mode": "markdown",
        "disable_web_page_preview": True
    }
    results = [
        {
            "type": "article",
            "id": str(x),
            "title": "test title " + str(x),
            "input_message_content": message,
            "description": "test description",
            "hide_url": True
        } for x in range(10)
    ]
    await iq.answer(results)
