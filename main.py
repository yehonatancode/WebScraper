import asyncio
import time

from modules.file_utils import read_file
from modules.pyppeteer_utils import get_webdriver, close
from operations.bbc import run_bbc
from operations.flight_table import run_flight_table
from pages.flight_table import FlightTablePage



async def main():
    # Lunch browser
    browser, page = await get_webdriver(headless=True)

    # await run_bbc(page) - use only one of the two each time.

    await run_flight_table(page)

    await close(browser)


asyncio.get_event_loop().run_until_complete(main())
