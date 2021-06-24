import unittest

from app.db.models import Base, Article, ArticleLink, ArticleTag

from datetime import datetime as dt

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class testORM(unittest.TestCase):
    
    article1 = {
        'url': 'url1',
        'title': 'title1',
        'date': dt.fromisoformat('2020-01-01'),
        'body': 'body1',
        'author': 'author1'
    }
    article2 = {
        'url': 'url2',
        'title': 'title2',
        'date': dt.fromisoformat('2020-01-01'),
        'body': 'body2'
    }
    article3 = {
        'url': 'url3',
        'title': 'title3',
        'date': dt.fromisoformat('2020-01-01'),
        'body': 'body3'
    }
    articleDuplicate1 = {
        'url': 'url1',
        'title': 'title2',
        'date': dt.fromisoformat('2020-01-01'),
        'body': 'body1'
    }
    
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
                )
            )
        Base.query = self.session.query_property()
        Base.metadata.create_all(bind=self.engine)

    def testArticles(self):
        a1 = Article(
            url = self.article1['url'],
            title = self.article1['title'],
            date = self.article1['date'],
            body = self.article1['body'],
        )

        
    
    def tearDown(self):
        self.session.remove()

