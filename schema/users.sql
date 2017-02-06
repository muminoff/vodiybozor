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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: users; Type: TABLE; Schema: public; Owner: sardor
--

CREATE TABLE users (
    id bigint NOT NULL,
    first_name text,
    last_name text,
    username text,
    joined timestamp without time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE users OWNER TO sardor;

--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: sardor
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

