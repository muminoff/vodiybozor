/* --------------- */
/* drop all tables */
/* --------------- */
/* drop table subscribers; */
/* drop table contacts; */
/* drop table drafts; */
/* drop table ads; */
/* drop table categories; */
/* drop table visitors; */
/* drop table users; */
/* \q */

/* ---------------- */
/* citext extension */
/* ---------------- */
create extension if not exists citext;
create extension if not exists pg_hahids;

/* ----------- */
/* users table */
/* ----------- */
create table if not exists users (
  id bigint primary key,
  first_name citext not null,
  last_name citext,
  username citext unique,
  is_admin boolean default false,
  is_active boolean default true,
  joined timestamptz default timezone('Asia/Tashkent'::text, now())
);
create view new_users as select id, first_name, last_name, username, joined from users where extract(day from joined) = extract(day from current_date) order by joined desc;

/* ----------- */
/* users index */
/* ----------- */
create index active_users_idx on users (is_active) where (is_active=true);
create index inactive_users_idx on users (is_active) where (is_active=false);
create index admin_users_idx on users (is_active) where (is_admin=true);
create index users_username_idx on users using btree (lower(username));
create index users_first_name_idx on users using btree (lower(first_name));
create index users_last_name_idx on users using btree (lower(last_name));

/* ---------------- */
/* categories table */
/* ---------------- */
create table if not exists categories (
  id smallserial primary key,
  name citext,
  created timestamptz default timezone('Asia/Tashkent'::text, now())
);

/* ------ */
/* Dump   */
/* ------ */
COPY categories (name) FROM stdin;
Авто-улов
Кўчмас-мулк
Маиший техника
Уй-рўзғор буюмлари
Кийим-кечак
Спорт анжомлари
Телефон
\.

/* ------------ */
/* drafts table */
/* ------------ */
create table if not exists drafts (
  id text primary key,
  data jsonb,
  created timestamptz default timezone('Asia/Tashkent'::text, now())
);

/* --------- */
/* ads table */
/* --------- */
create table if not exists ads (
  id bigserial primary key,
  category_id smallint references categories(id),
  user_id bigint references users(id),
  data jsonb,
  is_closed bool default false,
  is_published bool default false,
  created timestamptz default timezone('Asia/Tashkent'::text, now())
);

/* --------- */
/* ads index */
/* --------- */
create index closed_ads_idx on ads (is_closed) where (is_closed=true);
create index published_ads_idx on ads (is_published) where (is_published=true);
create index ads_data_name_idx on ads using gin (((data -> 'name'::text)));
create index ads_data_contact on ads using gin (((data -> 'contact'::text)));

/* ----------------- */
/* subscribers table */
/* ----------------- */
create table if not exists subscribers (
  category_id bigint references categories(id),
  user_id bigint references users(id),
  subscribed_at timestamptz default timezone('Asia/Tashkent'::text, now()),
  primary key (category_id, user_id)
);

/* -------------- */
/* contacts table */
/* -------------- */
create table if not exists contacts (
  user_id bigint references users(id) unique,
  phone_number text,
  created timestamptz default timezone('Asia/Tashkent'::text, now())
);
create index contacts_phone_number_idx on contacts using btree (phone_number);

/* -------------- */
/* visitors table */
/* -------------- */
create table visitors (
  id bigserial primary key,
  timestamp timestamptz default timezone('Asia/Tashkent'::text, now()),
  user_id bigint references users(id),
  message jsonb);
create index visitors_timestamp_idx on visitors (timestamp);
create index visitors_message_first_name_idx on visitors using gin (((message -> 'chat' -> 'first_name'::text)));
create index visitors_message_text_idx on visitors using gin (((message -> 'text'::text)));
create view last_visitors as select timestamp, message -> 'chat' ->> 'first_name' as visitor, message -> 'text' as text  from visitors order by timestamp limit 50;

/* ------------------ */
/* event notification */
/* ------------------ */
create or replace function notify_event() returns trigger as $$
  declare
    data json;
    notification json;
  begin
    if (TG_OP = 'DELETE') then
      data = row_to_json(OLD);
    else
      data = row_to_json(NEW);
    end if;

    notification = json_build_object(
                      'table', TG_TABLE_NAME,
                      'action', lower(TG_OP),
                      'data', data);
    perform pg_notify('events', notification::text);
    return null
  end;
$$ language plpgsql;

/* ------------------ */
/* users notification */
/* ------------------ */
create trigger users_notify_event
after insert or update or delete on users
for each row execute procedure notify_event();

/* ------------------- */
/* drafts notification */
/* ------------------- */
create trigger drafts_notify_event
after insert or update or delete on drafts
for each row execute procedure notify_event();

/* ------------------- */
/* drafts notification */
/* ------------------- */
create trigger drafts_notify_event
after insert or update or delete on drafts
for each row execute procedure notify_event();
