CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS products (
    id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    type uuid REFERENCES product_types(id),
    data jsonb,
    is_sold bool DEFAULT false,
    is_published bool DEFAULT false,
    written_by bigint REFERENCES users(id),
    created timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);
    /* name text, */
    /* year integer, */
    /* price numeric, */
    /* mill text, */
    /* contact bigint, */
    /* username text, */
    /* image_url text, */
