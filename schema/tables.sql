/* --------------- */
/* drop all tables */
/* --------------- */
/* drop table subscribers; */
/* drop table drafts; */
/* drop table ads; */
/* drop table categories; */
/* drop table users; */

/* ---------------- */
/* citext extension */
/* ---------------- */
create extension if not exists citext;

/* ----------- */
/* users table */
/* ----------- */
create table if not exists users (
    id bigint primary key,
    first_name citext,
    last_name citext,
    username citext,
    is_admin boolean default false,
    is_active boolean default true,
    joined timestamptz default timezone('Asia/Tashkent'::text, now())
);

/* ----------- */
/* users index */
/* ----------- */
create index active_users_idx on users (is_active) where (is_active=true);
create index inactive_users_idx on users (is_active) where (is_active=false);
create index admin_users_idx on users (is_active) where (is_admin=true);
create index users_username_idx on users using btree (username);
create index users_first_name_idx on users using btree (first_name);
create index users_last_name_idx on users using btree (last_name);

/* ---------------- */
/* categories table */
/* ---------------- */
create table if not exists categories (
    id smallserial primary key,
    name citext,
    created timestamptz default timezone('Asia/Tashkent'::text, now())
);

/* ------------ */
/* drafts table */
/* ------------ */
create table if not exists drafts (
    id bigserial primary key,
    category_id smallint references categories(id),
    user_id bigint references users(id),
    data jsonb,
    created timestamptz default timezone('Asia/Tashkent'::text, now())
);

/* --------- */
/* ads table */
/* --------- */
create table if not exists ads (
    id bigserial primary key,
    category_id smallint references categories(id),
    user_id bigint references users(id),
    data jsonb,
    is_closed bool default false,
    is_published bool default false,
    created timestamptz default timezone('Asia/Tashkent'::text, now())
);

/* --------- */
/* ads index */
/* --------- */
create index closed_ads_idx on ads (is_closed) where (is_closed=true);
create index published_ads_idx on ads (is_published) where (is_published=true);
create index ads_data_name_idx on ads using gin (((data -> 'name'::text)));
create index ads_data_contact on ads using gin (((data -> 'contact'::text)));

/* ----------------- */
/* subscribers table */
/* ----------------- */
create table if not exists subscribers (
    category_id bigint references categories(id),
    user_id bigint references users(id),
    subscribed_at timestamptz default timezone('Asia/Tashkent'::text, now()),
    primary key (category_id, user_id)
);

/* -------------- */
/* contacts table */
/* -------------- */
/* {'phone_number': '821035027155', 'first_name': 'Sardor', 'user_id': 56781796} */
create table if not exists contacts (
    user_id bigint references users(id) unique,
    phone_number text,
    created timestamptz default timezone('Asia/Tashkent'::text, now())
);
create index contacts_phone_number_idx on contacts using btree (phone_number);
