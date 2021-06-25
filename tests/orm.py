import unittest

import sqlalchemy

from app.db import models

from datetime import datetime as dt

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os

load_dotenv()

class testORM(unittest.TestCase):
    
    a1 = {
        'url': 'url1',
        'title': 'title1',
        'date': dt.fromisoformat('2020-01-01'),
        'body': 'body1',
        'author': 'author1'
    }
    a2 = {
        'url': 'url2',
        'title': 'title2',
        'date': dt.fromisoformat('2020-01-01'),
        'body': 'body2'
    }
    a3 = {
        'url': 'url3',
        'title': 'title3',
        'date': dt.fromisoformat('2020-01-01'),
        'body': 'body3'
    }
    a1d = {
        'url': 'url1',
        'title': 'title2',
        'date': dt.fromisoformat('2020-01-01'),
        'body': 'body1'
    }
    
    def __init__(self, *args, **kwargs):
        super(testORM, self).__init__(*args, **kwargs)
        
        self.engine = create_engine(os.getenv('DB_URI_TEST'))
        models.Base.metadata.create_all(self.engine)
        self.session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
                )
            )
        # models.Base.query = self.session.query_property()
        
    def test_articles(self):
        s = self.session()
        models.insert_article(article=self.a1, session=s)
        s.commit()
        r = s.query(models.Article).all()
        self.assertEqual(len(r), 1)
        self.assertNotEqual(r[0].id, None)
        print(r)
        models.insert_article(self.a1d, s)
        r = s.query(models.Article).all()
        print(r)
        print(models.insert_article(self.a1d, s))
        # self.assertRaises(models.insert_article(self.a1d, s), sqlalchemy.exc.SQLAlchemyError)

    
    def tearDown(self):
        self.session.remove()
        models.Base.metadata.drop_all(self.engine)

