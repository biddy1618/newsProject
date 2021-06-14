import unittest

import random

import requests

from crawler import Crawler
from helper import Helper
from bs4 import BeautifulSoup as bs

class Test(unittest.TestCase):
    
    def testLinksRetrieved(self):
        
        crawler = Crawler()
        dates = Helper.generate_dates("01.01.2019", "01.02.2021")
        
        res = set()

        for d in random.sample(dates, 20):
            r = crawler.get_url(crawler.URL_ARCHIVE, {'date': d})
            self.assertEqual(r.status_code, 200)
            
            links = crawler.extract_links(r)
            self.assertEqual(len(links), 20)
            res.update(links)
        self.assertEqual(len(res), 20 * 20)

    def testArticlesRetrieved(self):
        
        crawler = Crawler()
        dates = Helper.generate_dates("01.01.2019", "01.02.2021")
        
        res = set()

        for d in random.sample(dates, 10):
            r = crawler.get_url(
                crawler.URL_ARCHIVE,
                {'date': d}
            )
            self.assertEqual(r.status_code, 200)
        
            links = crawler.extract_links(r)
            self.assertEqual(len(links), 20)
        
            for l in random.sample(links, 2):
                link_url = crawler.URL_MAIN + l
                body = requests.get(link_url)

                soup = bs(body.content, 'html.parser')

                title = soup.find('div', class_ = 'article_title')
                self.assertIsNotNone(title)
                self.assertIsInstance(title.getText().strip(), str)

                date = soup.find('div', class_ = 'date_public_art')
                self.assertIsNotNone(date)
                self.assertIsInstance(date.getText().strip(), str)
                
                links = soup.find('div', class_ = 'frame_news_article')
                if links is not None: links.decompose()
                
                body = soup.find('div', class_ = 'article_news_body')
                self.assertIsNotNone(body)
                self.assertIsInstance(body.getText().strip(), str)