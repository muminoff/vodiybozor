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
    INSERT INTO users(id, first_name, last_name, username, is_active)
    VALUES ($1, $2, $3, $4, $5)
    ON CONFLICT (id)
    DO UPDATE SET (first_name, last_name, username, is_active) = ($2, $3, $4, $5)
    '''

    conn = await pool.acquire()

    try:
        id = user.get('id')
        first_name = user.get('first_name')
        last_name = user.get('last_name', '')
        username = user.get('username', '')
        is_active = True
        await conn.execute(query, id, first_name, last_name, username, is_active)

    finally:
        await pool.release(conn)


async def deactivate_user(pool, user):
    query = '''
    UPDATE users
    SET is_active=false
    WHERE id=$1
    '''

    conn = await pool.acquire()

    try:
        id = user.get('id')
        await conn.execute(query, id)

    finally:
        await pool.release(conn)