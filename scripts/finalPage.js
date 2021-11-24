() => {
    const nextBtn = "#next"
    const currentElement = "#numOfResults";
    const totalElement = "#totalItems"

    function isMorePages() {
        const current = document.querySelector(currentElement);
        const total = document.querySelector(totalElement);

        return (!current || !total) || current.textContent !== total.textContent;
    }

    function getButton() {
        const button = document.querySelector(nextBtn);

        return button && button.style.display !== "none" ? button : null
    }

    function clickButton() {
        const button = getButton();
        if (button && isMorePages()) {
            button.click();
            return true;
        }

        return false;
    }

    return clickButton();
}
