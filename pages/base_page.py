from pyppeteer.page import Page


class BasePage:
    def __init__(self, page: Page, url: str):
        self._page = page
        self._url = url

    def navigate_to_url(self, url: str = ""):
        target_url = url or self._url

        print(f"Navigation to {target_url}...")
        return self._page.goto(target_url)

    def execute_script(self, src: str, msg: str = ""):
        if msg:
            print(msg)
        return self._page.evaluate(src)

    def wait_for_selector(self, selector: str, timeout=20000, msg=""):
        print(f"{msg}" if msg else f"Waiting for {selector}..., attempt")

        return self._page.waitForSelector(selector=selector, timeout=timeout)
