# @bot.command(r'/boshla')
# async def broadcast(chat, match):
#     # EXPERIMENTAL
#     logger.info('Broadcast requested by %s', chat.sender)

#     if not await user_is_admin(chat.bot.pg_pool, chat.sender):

#         info = format_text('''
#         Сиз админ эмассиз.
#         ''')
# await chat.send_text(info, parse_mode='Markdown',
# disable_web_page_preview=True)

#         info = format_text('''
#         Узр ома.
#         ''')
# await chat.send_text(info, parse_mode='Markdown',
# disable_web_page_preview=True)

#         return

#     users = await get_all_admins(chat.bot.pg_pool)
#     await chat.send_text('%d та хабар юбораман.' % len(users))

#     import time
#     start = time.time()

#     for user in users:
#         logger.info('Sending to %s (%s)', user['first_name'], user['username'])
#         # text = format_text('''
#         # Яна бир бор ассалому алайкум, {name}.

#         # Яқин кунларда ишга тушаман. Шунга ўзим бир текшириб кўрмоқчидим. 😊
#         # ''')
#         text = '{name} test'
#         ch = chat.bot.private(user['id'])
#         # try:
#         await ch.send_text(text.format(name=user['first_name']))
#         # except:
#         #     logger.info('Cannot send to %s', user)
#         #     pass

#     logger.info('{0:0.4f} time spent to broadcast message to {1} users'.format((time.time() - start), len(users)))
#     await chat.send_text('Хабарлар юборилди.')
