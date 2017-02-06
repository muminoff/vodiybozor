CREATE TABLE users (
    id bigint NOT NULL,
    first_name text,
    last_name text,
    username text,
    joined timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);
