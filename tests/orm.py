import unittest

from app.db.models import Article, Articlelink, Articletag
from app.db.db import Session
from datetime import datetime as dt

class testORM(unittest.TestCase):
    article1 = {
        'url': 'url1',
        'title': 'title1',
        'date': dt.fromisoformat('2020-01-01'),
        'article': 'body1',
        'author': 'author1'
    }
    article2 = {
        'url': 'url2',
        'title': 'title2',
        'date': dt.fromisoformat('2020-01-01'),
        'article': 'body2'
    }
    article3 = {
        'url': 'url3',
        'title': 'title3',
        'date': dt.fromisoformat('2020-01-01'),
        'article': 'body3'
    }
    articleDuplicate1 = {
        'url': 'url1',
        'title': 'title2',
        'date': dt.fromisoformat('2020-01-01'),
        'article': 'body1'
    }

    def __init__(self):
        self.session = Session()
        self.session.query(Article).filter_by(url = self.article1['url'])

    def testArticles(self):
        a1 = Article(
            url = self.article1['url'],
            title = self.article1['title'],
            date = self.article1['date'],
            article = self.article1['article'],
        )
        session.add(a1)
