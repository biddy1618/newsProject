import unittest

import random

import requests

from crawler import Crawler
from helper import Helper
from bs4 import BeautifulSoup as bs

class TestLinks(unittest.TestCase):
    # def testRandomPagesForLinks(self):
    #     url = "https://www.inform.kz/ru/archive"

    #     crawler = Crawler()
    #     dates = Helper.generateDates("01.01.2019", "01.02.2021")
        
    #     for d in random.sample(dates, 20):
    #         r = crawler.getUrl(url, {'date': d})
    #         self.assertEqual(r.status_code, 200)
    
    def testLinksRetrieved(self):
        url = "https://www.inform.kz/ru/archive"

        crawler = Crawler()
        dates = Helper.generateDates("01.01.2019", "01.02.2021")
        
        res = set()

        for d in random.sample(dates, 20):
            r = crawler.getUrl(url, {'date': d})
            self.assertEqual(r.status_code, 200)
            
            links = crawler.extractLinks(r)
            self.assertEqual(len(links), 20)
            res.update(links)
        self.assertEqual(len(res), 20 * 20)

    
