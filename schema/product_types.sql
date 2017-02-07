CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE product_types;
CREATE TABLE product_types (
    id uuid DEFAULT uuid_generate_v4() NOT NULL,
    name text,
    created timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);
