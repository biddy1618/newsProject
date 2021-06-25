create table if not exists Articles (
    id int primary key generated always as identity,
    url varchar unique not null,
    title varchar unique not null,
    date date not null,
    body varchar not null,
    author varchar
);

create table if not exists Article_links (
    id int primary key generated always as identity,
    id_article integer not null references Articles,
    id_article_other integer not null
);

create table if not exists Article_tags (
    id int primary key generated always as identity,
    id_article integer not null references Articles,
    tag varchar not null
);