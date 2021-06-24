# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship, Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declared_attr

from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declarative_base

from decimal import Decimal as D

from typing import List
from app.helper import Helper
import logging

import json

Base = declarative_base()

class BaseH(object):
    
    @declared_attr
    def __tablename__(self):
        return self.__class__.__name__.lower()

    id =  Column(Integer, primary_key=True)

    def serialize(self):
        return {c.name: getattr(self, c.name) for c in inspect(self.__class__).c}

    def update(self, data):
        for k, v in data.items():
            setattr(self, k, v)
    
    @staticmethod
    def serializeStatic(row):
        return {c: BaseH.checkDecimal(getattr(row, c)) 
                for c in row.keys()}
    
    @staticmethod
    def checkDecimal(val):
        return str(val) if isinstance(val, D) else val
    

class Article(Base, BaseH):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, server_default=text("nextval('articles_id_seq'::regclass)"))
    url = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False, unique=True)
    date = Column(Date, nullable=False)
    body = Column(String, nullable=False)
    author = Column(String)

    def __repr__(self):
        return f'Article: "{self.url}"'


class ArticleLink(Base, BaseH):
    __tablename__ = 'article_links'

    id = Column(Integer, primary_key=True, server_default=text("nextval('article_links_id_seq'::regclass)"))
    id_article = Column(ForeignKey('articles.id'), nullable=False)
    id_article_other = Column(ForeignKey('articles.id'), nullable=False)

    article = relationship('Article', primaryjoin='ArticleLink.id_article == Article.id')
    article1 = relationship('Article', primaryjoin='ArticleLink.id_article_other == Article.id')

    def __repr__(self):
        return f'Link: "{self.article.url}" -> "{self.article1.url}"'


class ArticleTag(Base, BaseH):
    __tablename__ = 'article_tags'

    id = Column(Integer, primary_key=True, server_default=text("nextval('article_tags_id_seq'::regclass)"))
    id_article = Column(ForeignKey('articles.id'), nullable=False)
    tag = Column(String, nullable=False)

    article = relationship('Article')

    def __repr__(self):
        return f'Tag: "{self.tag}" linked to "{self.article.url}"'

logging.basicConfig(
    format='{levelname:<10} {asctime}: {message}', 
    level=logging.INFO, 
    datefmt='%m/%d/%Y %H:%M:%S',
    style='{')
logger = logging.getLogger(__name__)


def insertArticle(article: dict, session: Session) -> Article:
    try:
        a = Article(
            url = article['url'],
            title = article['title'],
            date = article['date'],
            body = article['body'],
        )
        if 'author' in article: a.author = article['author']
        session.add(a)
    except AttributeError as e:
        logger.error(Helper._message(f'Failed to get attributes while inserting article: {article}', e))
        raise SystemExit(e)
    except SQLAlchemyError as e:
        logger.error(Helper._message(f'SQLAlchemy error at insertion of the following article: {article}', e))
        raise SystemExit(e)

    return a

def insertArticleBulk(articles: list, session: Session) -> List[Article]:
    res = []

    for a in articles:
        res.append(insertArticle(a, session))
    
    return res

def get_article_by_url(url: str, session: Session) -> Article:
    a = session.query(Article).filter_by(url = url).first()
    return a

def insert_link(urls: dict, session: Session) -> ArticleLink:
    try:
        article1 = get_article_by_url(urls['url_main'], session)
        article2 = get_article_by_url(urls['url_other'], session)
    except AttributeError as e:
        logger.error(Helper._message(f'Failed to get URL attributes while inserting link: {urls}', e))
        raise SystemExit(e)
    try:
        l = ArticleLink(
            id_article = article1.id,
            id_article_other = article2.id
        )
        session.add(l)
    except AttributeError as e:
        logger.error(Helper._message(f'Failed to find the articles IDs with URLs: {urls}', e))
        raise SystemExit(e)
    except SQLAlchemyError as e:
        logger.error(Helper._message(f'SQLAlchemy error at insertion of the following link: {urls}', e))
        raise SystemExit(e)
    
    return l

def insert_tag(url_tag: dict, session: Session) -> ArticleTag:
    try:
        article = get_article_by_url(url_tag['url'], session)
        tag = url_tag['tag']
    except AttributeError as e:
        logger.error(Helper._message(f'Failed to get tag attributes while inserting tag: {url_tag}', e))
        raise SystemExit(e)
    try:
        t = ArticleTag(
            id_article = article.id,
            tag = tag
        )
        session.add(t)
    except AttributeError as e:
        logger.error(Helper._message(f'Failed to find the article ID with URL: {url_tag["url"]}', e))
        raise SystemExit(e)
    except SQLAlchemyError as e:
        logger.error(Helper._message(f'SQLAlchemy error at insertion of the following link: {url_tag}', e))
        raise SystemExit(e)
    
    return t