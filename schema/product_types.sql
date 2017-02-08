CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS product_types (
    id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    name text,
    created timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);

COPY product_types (id, name, created) FROM stdin;
04aaa79c-c335-445d-b190-98690ddd71dc	Телефон	2017-02-07 06:46:03.239643
5e675d76-d1e8-4594-96b6-c1b3f38a237c	Автотранспорт	2017-02-07 06:46:42.464734
6f228530-0cdd-48bd-a6b1-d6505e278e62	Кўчмас мулк	2017-02-07 06:47:25.294613
\.
