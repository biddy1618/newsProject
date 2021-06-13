import requests
from bs4 import BeautifulSoup as bs

from typing import Dict, List

class Crawler():
    """
    Generic class defining crawler
    """
    def getUrl(sefl, url: str, params: Dict[str, str]) -> requests.Response:
        """
        Fetch the URL provided and return response object

        Args:
            url (str): URL provided
            params (Dict[str, str]): query parameters in dictinary format

        Returns:
            requests.Response: HTML page fetched with response code
        """
        body = requests.get(url, params = params)
        return body

    def extractLinks(self, body: requests.Response) -> List[str]:
        """
        Retrieving links given the response object

        Args:
            body (requests.Response): response object containing links to articles

        Returns:
            List[str]: list of extractred article links give the reponse
        """
        soup = bs(body.content, 'html.parser')
        link_divs = soup.find_all('div', class_ = 'lenta_news_block')
        links = [d.li.a['href'].strip() for d in link_divs]

        return links
    
    def extractArticle(self, body: requests.Response) -> Dict[str, str]:
        """[summary]

        Args:
            body (requests.Response): [description]

        Returns:
            Dict[str, str]: [description]
        """
        raise NotImplementedError("Function not implemented yet.")


