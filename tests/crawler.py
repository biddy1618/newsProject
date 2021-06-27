import unittest
import random
import logging

from app.crawler.crawler import Crawler
from app.helper import Helper



logger = logging.getLogger(__name__)

class TestCrawler(unittest.TestCase):
    invalid = 'invalid'

    def testCrawler(self):
        """
        Testing crawler functions.
        """
        self.assertEqual(Helper.generate_dates('invalid'), None)
        self.assertEqual(Helper.generate_dates('01.01.2020', 'invalid'), None)
        self.assertEqual(Helper.generate_dates('01.01.2020', '01.01.2019'), None)
        self.assertEqual(Helper.generate_dates('01.01.2020', '01.01.2020'), None)

        dates = Helper.generate_dates('01.01.2019', '02.01.2020')
        self.assertNotEqual(dates, None)
        
        crawler = Crawler()
        try:
            self.assertEqual(crawler.get_url(self.invalid), None)
            self.assertEqual(crawler.get_url(self.invalid, {}), None)
            self.assertEqual(crawler.get_url(self.invalid, {'date': self.invalid}), None)
            # Following test fails since web-site actually return page even if the parameters are wrong
            # self.assertEqual(crawler.get_url(crawler.URL_ARCHIVE, {'date': self.invalid}), None)
            
            for d in random.sample(dates, 1):
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
                    if 'tags' in article:
                        self.assertIsInstance(article['tags'], list)
                    if 'author' in article:
                        self.assertIsInstance(article['author'], str)
        finally:
            crawler.close()
        
    
