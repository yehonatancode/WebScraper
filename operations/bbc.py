from typing import List

import requests
from bs4 import BeautifulSoup
from pyppeteer.page import Page

from modules.file_utils import read_file
from pages.bbc_page import BBCPage

SITE_URL = "https://www.bbc.com/"


async def run_bbc(page: Page):
    bbc = BBCPage(page=page, url=SITE_URL)

    await bbc.navigate_to_url()

    # await run_flight_table(page)
    scrape_articles_script = read_file("scripts/scrapeArticles.js")

    articles: List[dict] = await bbc.execute_script(scrape_articles_script, msg="scraping articles...")

    for article in articles:
        response = requests.get(article.get("url"))
        text = ' '.join(BeautifulSoup(response.text, 'html.parser').stripped_strings)
        article["full_text"] = text

    bbc.set_articles(articles)

    return True
