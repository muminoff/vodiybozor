--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.2
-- Dumped by pg_dump version 9.5.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: sardor
--

COPY category (id, name, created) FROM stdin;
1	Авто-улов	2017-02-15 09:44:09.350695
2	Кўчмас-мулк	2017-02-15 09:45:50.401334
3	Маиший техника	2017-02-15 09:45:57.799454
4	Уй рўзғор буюмлари	2017-02-15 09:46:11.99206
5	Кийим-кечак	2017-02-15 09:46:23.475685
6	Спорт анжомлари	2017-02-15 09:46:30.981122
7	Телефон	2017-02-15 09:46:35.262073
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sardor
--

SELECT pg_catalog.setval('category_id_seq', 7, true);


--
-- PostgreSQL database dump complete
--

