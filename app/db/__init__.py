from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, create_session
from sqlalchemy.ext.declarative import declarative_base

from flask import g

from app.db import models

engine = None
db_session = scoped_session(lambda: create_session(bind=engine))

def get_session():
    if 's' not in g:
        g.s = db_session()
    return g.s

def close_session(exception = None):
    s = g.pop('s', None)

    if s is not None:
        db_session.remove()

def init_db(app):
    global engine
    engine = create_engine(app.config['DATABASE'])
    models.Base.metadata.create_all(engine)

    app.teardown_appcontext(close_session)