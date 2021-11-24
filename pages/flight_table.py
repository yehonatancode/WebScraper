import json
from typing import List

from pyppeteer.page import Page

from pages.base_page import BasePage

ID_FIELD = "טיסה"
FILE = "output/flights.json"

class FlightTablePage(BasePage):
    def __init__(self, page: Page, url: str):
        super().__init__(page, url)
        self._flights = []
        self._ids = set()

    def _set_ids(self, latest: List[dict]):
        self._ids = set()
        for flight in latest:
            self._ids.add(flight.get(ID_FIELD))

    def _save(self):
        text = json.dumps(self._flights, ensure_ascii=False, indent=4)

        with open(FILE, 'wb') as file:
            file.write(text.encode('utf-8'))

    def _update_flights(self, latest: List[dict]):
        new_flights = [flight for flight in latest if flight.get(ID_FIELD, None) and flight.get(ID_FIELD) not in self._ids]

        self._flights = new_flights + self._flights

    def set_flights(self, latest: List[dict]):
        if not self._flights:
            self._flights = latest
        else:
            self._update_flights(latest)

        self._set_ids(self._flights)

        self._save()

        print("Latest Flights:")
        print(self._flights)

    def search(self, query: str):
        lower = query.lower().strip()

        found = []
        for flight in self._flights:
            for value in flight.values():
                if lower in str(value).lower():
                    found.append(flight)
                    break

        return found
