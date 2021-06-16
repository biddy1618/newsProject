import requests
from bs4 import BeautifulSoup as bs

from typing import Dict, List

class Crawler():

    def __init__(self) -> None:
        self.URL_MAIN = "https://www.inform.kz"
        self.URL_ARCHIVE = "https://www.inform.kz/ru/archive"
    """
    Generic class defining crawler
    """
    def get_url(sefl, url: str, params: Dict[str, str]) -> requests.Response:
        """
        Fetch the URL provided and return response object

        Args:
            url (str): URL provided
            params (Dict[str, str]): query parameters in dictinary format

        Returns:
            requests.Response: HTML page fetched with response code
        """
        body = None
        try:
            body = requests.get(url, params = params)
        except Exception as e:
            "TODO: set up logging for failed fetch"
            print(e)

        return body

    def extract_links(self, body: requests.Response) -> List[str]:
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
    
    def extract_article(self, body: requests.Response) -> Dict[str, str]:
        """[summary]

        Args:
            body (requests.Response): [description]

        Returns:
            Dict[str, str]: [description]
        """
        raise NotImplementedError("Function not implemented yet.")


