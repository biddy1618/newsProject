create table if not exists Articles (
    id serial primary key,
    url varchar unique not null,
    title varchar unique not null,
    date date not null,
    body varchar not null,
    author varchar
);

create table if not exists Article_links (
    id serial primary key,
    id_article integer not null references Articles,
    id_article_other integer not null
);

create table if not exists Article_tags (
    id serial primary key,
    id_article integer not null references Articles,
    tag varchar not null
);