async def user_exists(pool, user):
    query = '''
    SELECT EXISTS(SELECT id FROM users WHERE id=$1)
    '''
    conn = await pool.acquire()

    try:
        id = user.get('id')
        result = await conn.fetchval(query, id)

    finally:
        await pool.release(conn)

    return result


async def insert_user(pool, user):
    query = '''
    INSERT INTO users(id, first_name, last_name, username)
    VALUES ($1, $2, $3, $4)
    ON CONFLICT (id)
    DO UPDATE SET (first_name, last_name, username) = ($2, $3, $4)
    '''

    conn = await pool.acquire()

    try:
        id = user.get('id')
        first_name = user.get('first_name')
        last_name = user.get('last_name', '')
        username = user.get('username', '')
        await conn.execute(query, id, first_name, last_name, username)

    finally:
        await pool.release(conn)
