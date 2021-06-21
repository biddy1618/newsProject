# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, String, text
from sqlalchemy.engine import base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declared_attr

from decimal import Decimal as D

from .db import Base

metadata = Base.metadata

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
    article = Column(String, nullable=False)
    author = Column(String)


class Articlelink(Base, BaseH):
    __tablename__ = 'articlelinks'

    id = Column(Integer, primary_key=True, server_default=text("nextval('articlelinks_id_seq'::regclass)"))
    idarticle = Column(ForeignKey('articles.id'), nullable=False, server_default=text("nextval('articlelinks_idarticle_seq'::regclass)"))
    url_other = Column(String, nullable=False)

    article = relationship('Article')


class Articletag(Base, BaseH):
    __tablename__ = 'articletags'

    id = Column(Integer, primary_key=True, server_default=text("nextval('articletags_id_seq'::regclass)"))
    idarticle = Column(ForeignKey('articles.id'), nullable=False, server_default=text("nextval('articletags_idarticle_seq'::regclass)"))
    tag = Column(String, nullable=False)

    article = relationship('Article')