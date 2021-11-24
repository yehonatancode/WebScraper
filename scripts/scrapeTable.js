() => {
    const TABLE_ID = "flight_board-arrivel_table"

    const getTextFromElement = (traget, selector) => {
        return [...traget.querySelectorAll(selector)].map(item => item.textContent.trim());
    }

    const table = document.getElementById(TABLE_ID);
    table.scrollIntoView();

    const rows =  table.querySelectorAll(`tbody tr`);

    let flights = [];

    for (const row of rows) {
        const items = row.querySelectorAll(`.field--wrapper`);

        const flight = {};
        for (const item of items) {
            const [header, value] = getTextFromElement(item, `div`);

            flight[header] = value;
        }

        flights.push(flight);
    }

    return flights;
}