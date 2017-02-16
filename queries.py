async def user_exists(pool, user):
    query = '''
    select exists(select id from users where id=$1)
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
    insert into users(id, first_name, last_name, username, is_active)
    values ($1, $2, $3, $4, $5)
    on conflict (id)
    do update set (first_name, last_name, username, is_active) = ($2, $3, $4, $5)
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


async def insert_contact(pool, contact):
    query = '''
    insert into contacts(user_id, phone_number)
    values ($1, $2)
    on conflict (user_id)
    do update set (phone_number) = ($2)
    '''

    conn = await pool.acquire()

    try:
        user_id = contact.get('user_id')
        phone_number = contact.get('phone_number')
        await conn.execute(query, user_id, phone_number)

    finally:
        await pool.release(conn)


async def insert_draft(pool, category_id, user_id, data):
    query = '''
    insert into drafts(category_id, user_id, data)
    values ($1, $2, $3)
    '''

    conn = await pool.acquire()

    try:
        await conn.execute(query, category_id, user_id, data)

    finally:
        await pool.release(conn)


async def user_has_draft(pool, category_id, user_id):
    query = '''
    select exists(select id from drafts where category_id=$1 and user_id=$2)
    '''

    conn = await pool.acquire()

    try:
        result = await conn.fetchval(query, category_id, user_id)

    finally:
        await pool.release(conn)

    return result


async def deactivate_user(pool, user):
    query = '''
    update users
    set is_active=false
    where id=$1
    '''

    conn = await pool.acquire()

    try:
        id = user.get('id')
        await conn.execute(query, id)

    finally:
        await pool.release(conn)
