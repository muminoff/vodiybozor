CREATE TABLE IF NOT EXISTS subscribers (
    product_type bigint REFERENCES product_types(id),
    user_id bigint REFERENCES users(id),
    subscribed_at timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now()),
    primary key (product_type, user_id)
);
