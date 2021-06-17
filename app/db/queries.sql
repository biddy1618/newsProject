create table if not exists Links (
    id serial primary key,
    url varchar unique not null,
);

create table if not exists Articles (
    url varchar primary key,
    title varchar unique not null,
    date date not null,
    article varchar not null,
    author varchar
);

create table if not exists ArticleLinks (
    id serial primary key,
    url varchar not null references Articles,
    url_other varchar not null
);

create table if not exists ArticleTags (
    id serial primary key,
    url varchar not null references Articles,
    tag varchar not null
);