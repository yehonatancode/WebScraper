from pyppeteer import launch


async def get_webdriver(headless: bool = False):
    browser = await launch(headless=headless, args=['--start-maximized', '--window-size=1920,1080'])
    page = await browser.newPage()

    await page.setViewport({"width": 1920, "height": 1080})

    return browser, page


def close(browser):
    return browser.close()
