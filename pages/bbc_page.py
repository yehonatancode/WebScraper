import json
from typing import List

from pyppeteer.page import Page

from pages.base_page import BasePage

FILE = "output/articles.json"


class BBCPage(BasePage):
    def __init__(self, page: Page, url: str):
        super().__init__(page, url)
        self._articles = []

    def set_articles(self, articles: List[dict]):
        self._articles = articles
        self._save()

    def _save(self):
        text = json.dumps(self._articles, ensure_ascii=False, indent=4)

        with open(FILE, 'wb') as file:
            file.write(text.encode('utf-8'))
