drop table if exists waitlist;
create table waitlist (
  id integer primary key autoincrement,
  email text not null
);