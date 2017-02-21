create table if not exists drafts (
  id text primary key,
  data jsonb,
  created timestamptz default timezone('Asia/Tashkent'::text, now())
);
