create table if not exists users (
    id bigint primary key,
    first_name text,
    last_name text,
    username text,
    is_admin boolean default false,
    is_active boolean default true,
    joined timestamp without time zone default timezone('asia/tashkent'::text, now())
);
