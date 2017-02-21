import json

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


async def get_all_users(pool):
    query = '''
    select id, username, first_name
    from users
    where is_admin=false and is_active=true
    '''

    conn = await pool.acquire()
    results = []

    try:
        results = await conn.fetch(query)
    finally:
        await pool.release(conn)

    return results


async def get_all_admins(pool):
    query = '''
    select id, username, first_name
    from users
    where is_admin=true
    '''

    conn = await pool.acquire()
    results = []

    try:
        results = await conn.fetch(query)
    finally:
        await pool.release(conn)

    return results


async def user_is_admin(pool, user):
    query = '''
    select is_admin
    from users
    where id=$1
    '''

    id = user.get('id')
    conn = await pool.acquire()
    ret = False

    try:
        ret = await conn.fetchval(query, id)
    finally:
        await pool.release(conn)

    return ret


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
    on conflict
    do nothing
    '''

    conn = await pool.acquire()

    try:
        await conn.execute(query, category_id, user_id, json.dumps(data))

    finally:
        await pool.release(conn)


async def user_has_any_draft(pool, user_id):
    query = '''
    select exists(select data from drafts where user_id=$1)
    '''

    conn = await pool.acquire()

    try:
        result = await conn.fetchval(query, user_id)

    finally:
        await pool.release(conn)

    return result


async def user_has_draft(pool, user_id):
    query = '''
    select exists(select data from drafts where id=hash_encode($1, 'vodiybozor'))
    '''

    conn = await pool.acquire()

    try:
        result = await conn.fetchval(query, user_id)

    finally:
        await pool.release(conn)

    return result


async def delete_draft(pool, user_id):
    query = '''
    delete drafts
    where id=hash_encode($1, 'vodiybozor')
    '''

    conn = await pool.acquire()

    try:
        await conn.execute(query, user_id)

    finally:
        await pool.release(conn)


async def get_draft_category(pool, user_id):
    query = '''
    select category_id
    from drafts
    where user_id=$1
    '''

    conn = await pool.acquire()

    try:
        result = await conn.fetchval(query, user_id)

    finally:
        await pool.release(conn)

    return result


async def get_draft(pool, user_id):
    query = '''
    select data
    from drafts
    where id=hash_encode($1, 'vodiybozor')
    '''

    conn = await pool.acquire()

    try:
        result = await conn.fetchval(query, user_id)

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


async def insert_visitor(pool, user, message):
    query = '''
    insert into visitors(user_id, message)
    values ($1, $2)
    '''

    conn = await pool.acquire()

    try:
        id = user.get('id')
        await conn.execute(query, id, json.dumps(message))

    finally:
        await pool.release(conn)
