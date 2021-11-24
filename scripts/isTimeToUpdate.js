() => {
    const TIME_SELECTOR = "#lastUpdateTime";

    const time = document.querySelector(TIME_SELECTOR);

    return time && time.textContent !== "{time}" ? time.textContent: "{time}"
}