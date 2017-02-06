CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE smartphones (
    id uuid DEFAULT uuid_generate_v4() NOT NULL,
    name text,
    year integer,
    price numeric,
    published timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);
