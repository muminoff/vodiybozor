create table if not exists users (
    id bigint primary key,
    first_name text,
    last_name text,
    username text,
    is_admin boolean default false,
    is_active boolean default true,
    joined timestamp default timezone('asia/tashkent'::text, now())
);

create table if not exists category (
    id smallserial primary key,
    name text,
    created timestamp default timezone('asia/tashkent'::text, now())
);

create table if not exists drafts (
    id bigserial primary key,
    category_id smallint references category(id),
    user_id bigint references users(id),
    data jsonb,
    created timestamp default timezone('asia/tashkent'::text, now())
);

create table if not exists ads (
    id bigserial primary key,
    category_id smallint references category(id),
    data jsonb,
    is_sold bool default false,
    is_published bool default false,
    user_id bigint references users(id),
    created timestamp default timezone('asia/tashkent'::text, now())
);

create table if not exists subscribers (
    category_id bigint references category(id),
    user_id bigint references users(id),
    subscribed_at timestamp default timezone('asia/tashkent'::text, now()),
    primary key (category_id, user_id)
);
