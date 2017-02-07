DROP TABLE users;
CREATE TABLE users (
    id bigint PRIMARY KEY,
    first_name text,
    last_name text,
    username text,
    is_admin boolean DEFAULT false,
    joined timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);
