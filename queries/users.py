import os
import asyncpg

async def connection():
    dsn = os.environ.get('DATABASE_URL')
    conn = await asyncpg.connect(dsn)
    return await conn


async def user_exists(user):
    query = '''
    SELECT EXISTS(SELECT id FROM users WHERE id=$1)
    '''
    conn = await connection()

    id = user.get('id')
    result = await conn.fetchval(query, id)
    await conn.close()
    return result


async def insert_user(user):
    query = '''
    INSERT INTO users(id, first_name, last_name, username, is_active)
    VALUES ($1, $2, $3, $4, $5)
    ON CONFLICT (id)
    DO UPDATE SET (first_name, last_name, username, is_active) = ($2, $3, $4, $5)
    '''

    conn = await connection()
    id = user.get('id')
    first_name = user.get('first_name')
    last_name = user.get('last_name', '')
    username = user.get('username', '')
    is_active = True
    await conn.execute(query, id, first_name, last_name, username, is_active)
    await conn.close()


async def deactivate_user(user):
    query = '''
    UPDATE users
    SET is_active=false
    WHERE id=$1
    '''

    conn = await connection()

    id = user.get('id')
    await conn.execute(query, id)
    await conn.close()


async def has_user_products(user):
    query = '''
    SELECT EXISTS(SELECT id FROM products WHERE written_by=$1)
    '''

    conn = await connection()

    id = user.get('id')
    result = await conn.fetchval(query, id)
    await conn.close()
    return result


async def is_user_admin(user):
    query = '''
    SELECT EXISTS(SELECT id FROM users WHERE id=$1 and is_admin IS TRUE);
    '''

    conn = await connection()

    id = user.get('id')
    result = await conn.fetchval(query, id)
    await conn.close()

    return result
