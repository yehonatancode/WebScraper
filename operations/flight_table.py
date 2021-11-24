import time

from pyppeteer.page import Page

from modules.file_utils import read_file
from pages.flight_table import FlightTablePage

SITE_URL = "https://www.iaa.gov.il/airports/ben-gurion/flight-board"
TABLE_ID = "#flight_board-arrivel_table"

async def run_flight_table(page: Page):
    # create page instance
    table_page = FlightTablePage(page=page, url=SITE_URL)

    # open & read script - table scraping javascript code - return the fights in the table as a list of dictionaries
    table_scrape_script = read_file("scripts/scrapeTable.js")
    # open & read script - open all pages in the table by clicking the "next" button
    open_all_script = read_file("scripts/finalPage.js")

    # navigate to page & wait for all to load
    await table_page.navigate_to_url()

    # wait for table to show
    await table_page.wait_for_selector(selector=f"{TABLE_ID} tbody tr", msg="Waiting for table to load")

    # scroll to the bottom of the page util button is gone and number of result is equal to the number of total results
    print("Loading all the available results...")
    while await table_page.execute_script(open_all_script):
        time.sleep(2)  # give the dom enough time to react to click

    # update flights - only if the time field was updated - check every 5 seconds
    latest_update = ""
    while True:
        # open & read script - check if it's time to update the flights
        time_to_update_script = read_file("scripts/isTimeToUpdate.js").replace("{time}", latest_update)

        # run the script - return the last update time
        new_latest_update = await table_page.execute_script(time_to_update_script, msg="Fetching last update time from page...")
        print(f"last_update_time is {latest_update}, site table contains data from {new_latest_update}")

        # compare the last known time to the new received time
        if latest_update != new_latest_update:
            fights = await table_page.execute_script(table_scrape_script, msg="Fetching latest flights from table...")
            table_page.set_flights(fights)
            latest_update = new_latest_update
        time.sleep(5)
