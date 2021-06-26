import unittest
import random
import logging

from app.crawler.crawler import Crawler
from app.helper import Helper

logger = logging.getLogger(__name__)

class TestCrawler(unittest.TestCase):

    def testCrawler(self):
        dates = Helper.generate_dates('01.01.2019', '02.01.2020')
        crawler = Crawler()
        
        for d in random.sample(dates, 5):
            r = crawler.get_url(crawler.URL_ARCHIVE, {'date': d})
            self.assertEqual(r.status_code, 200)
            
            links = crawler.get_links(r)
            
            for l in links:
                page = crawler.get_url(l)
                self.assertEqual(r.status_code, 200)
                article = crawler.extract_article(page)

                self.assertTrue('url' in article)
                self.assertTrue('title' in article)
                self.assertTrue('date' in article)
                self.assertTrue('body' in article)

                self.assertIsInstance(article['title'], str)
                self.assertIsInstance(article['date'], str)
                self.assertIsInstance(article['body'], str)
                
                if 'links' in article:
                    self.assertIsInstance(article['links'], list)
                if 'keywords' in article:
                    self.assertIsInstance(article['keywords'], list)
                if 'author' in article:
                    self.assertIsInstance(article['author'], str)
    
    
