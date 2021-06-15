# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from .db import Base

metadata = Base.metadata


class Article(Base):
    __tablename__ = 'articles'

    url = Column(String, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    date = Column(Date, nullable=False)
    article = Column(String, nullable=False)
    author = Column(String)


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True, server_default=text("nextval('links_id_seq'::regclass)"))
    url = Column(String, nullable=False, unique=True)


class Articlelink(Base):
    __tablename__ = 'articlelinks'

    id = Column(Integer, primary_key=True, server_default=text("nextval('articlelinks_id_seq'::regclass)"))
    url = Column(ForeignKey('articles.url'), nullable=False)
    url_other = Column(String, nullable=False)

    article = relationship('Article')


class Articletag(Base):
    __tablename__ = 'articletags'

    id = Column(Integer, primary_key=True, server_default=text("nextval('articletags_id_seq'::regclass)"))
    url = Column(ForeignKey('articles.url'), nullable=False)
    tag = Column(String, nullable=False)

    article = relationship('Article')
