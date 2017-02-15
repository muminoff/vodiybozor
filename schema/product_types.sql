create table if not exists product_types (
    id smallserial primary key,
    name text,
    created timestamp without time zone default timezone('asia/tashkent'::text, now())
);

