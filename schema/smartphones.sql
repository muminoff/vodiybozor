CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE smartphones;
CREATE TABLE smartphones (
    id uuid DEFAULT uuid_generate_v4() NOT NULL,
    name text,
    year integer,
    price numeric,
    mill text,
    contact bigint,
    username text,
    image_url text,
    is_sold bool DEFAULT false,
    is_published bool DEFAULT false,
    created timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);
