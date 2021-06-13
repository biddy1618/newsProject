create table if not exists Links (
    id serial primary key,
    link varchar unique not null
);