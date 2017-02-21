import asyncpg
import asyncio
import os
import json
import time
import logging


async def main():
    logger = logging.getLogger(__name__)
    start = time.time()
    dsn = os.environ.get('DATABASE_URL')
    conn = await asyncpg.connect(dsn)

    user_id = 56781796

    query = '''
    select is_admin from users where id=$1
    '''
    result = await conn.fetchval(query, user_id)
    print(result)
    print('{:0.4f} time spent'.format(time.time() - start))
    # category_id = 1
    # user_id = 56781796
    # data = {'name': 'Lacetti', 'year': ' 2015', 'mileage': ' 35000',
    #         'status': ' яхши', 'price': ' 7000', 'contact': ' +998931234567'}
    # query = '''
    # insert into drafts(category_id, user_id, data)
    # values ($1, $2, $3)
    # on conflict
    # do nothing
    # '''

    # d = json.dumps(data)
    # print('---------->', d)

    # await conn.execute(query, category_id, user_id, d)


    # user = {
    #     'id': 56781796,
    #     'first_name': 'Sardor',
    #     'last_name': '',
    #     'username': 'test'
    # }

    # if await user_exists(conn, id):
    #     print('User exists')
    #     await update_user(conn, id, user)

    await conn.close()


async def user_exists(conn, id):
    query = 'select exists(select id from users where id=$1)'
    result = await conn.fetchval(query, id)
    # await conn.close()
    return result

async def update_user(conn, id, user):
    query = '''
    INSERT INTO users(id, first_name, last_name, username)
    VALUES ($1, $2, $3, $4)
    ON CONFLICT (id)
    DO UPDATE SET (first_name, last_name, username) = ($2, $3, $4)
    '''
    await conn.execute(query, user['id'], user['first_name'], user['last_name'], user['username'])


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
