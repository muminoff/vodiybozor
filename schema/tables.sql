/* --------------- */
/* drop all tables */
/* --------------- */
/* drop table subscribers; */
/* drop table drafts; */
/* drop table ads; */
/* drop table category; */
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
    joined timestamp default timezone('utc+5'::text, now())
);

/* ----------- */
/* users index */
/* ----------- */
create index new_users_idx on users (date(joined));
create index active_users_idx on users (is_active) where (is_active=true);
create index inactive_users_idx on users (is_active) where (is_active=false);
create index admin_users_idx on users (is_active) where (is_admin=true);
create index users_username_idx on users using btree (username);

/* -------------- */
/* category table */
/* -------------- */
create table if not exists category (
    id smallserial primary key,
    name citext,
    created timestamp default timezone('utc+5'::text, now())
);

/* ------------ */
/* drafts table */
/* ------------ */
create table if not exists drafts (
    id bigserial primary key,
    category_id smallint references category(id),
    user_id bigint references users(id),
    data jsonb,
    created timestamp default timezone('utc+5'::text, now())
);

/* --------- */
/* ads table */
/* --------- */
create table if not exists ads (
    id bigserial primary key,
    category_id smallint references category(id),
    user_id bigint references users(id),
    data jsonb,
    is_closed bool default false,
    is_published bool default false,
    created timestamp default timezone('utc+5'::text, now())
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
    category_id bigint references category(id),
    user_id bigint references users(id),
    subscribed_at timestamp default timezone('utc+5'::text, now()),
    primary key (category_id, user_id)
);
