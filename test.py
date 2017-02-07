import asyncpg
import asyncio
import os



async def main():
    dsn = os.environ.get('DATABASE_URL')
    conn = await asyncpg.connect(dsn)
    id = 56781796
    user = {
        'id': 56781796,
        'first_name': 'Sardor',
        'last_name': '',
        'username': 'test'
    }

    if await user_exists(conn, id):
        print('User exists')
        await update_user(conn, id, user)

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
