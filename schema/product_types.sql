CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS product_types (
    id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    name text,
    created timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);

