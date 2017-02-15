create table if not exists products (
    id bigserial primary key,
    type smallint references product_types(id),
    data jsonb,
    is_sold bool default false,
    is_published bool default false,
    written_by bigint references users(id),
    created timestamp without time zone default timezone('asia/tashkent'::text, now())
);

