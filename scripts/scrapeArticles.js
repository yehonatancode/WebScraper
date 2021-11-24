() => {
    const SELECTOR = 'li.media-list__item'

    const articleElements = document.querySelectorAll(SELECTOR);
    const articles = []

    function getTextInElement(target, selectors) {
        for (const selector of selectors) {
            const element = target.querySelector(selector);
            if (element) {
                return element.textContent.trim()
            }
        }

        return "";
    }

    function getAttributeInElement(target, selectors) {
        for (const selector of selectors) {
            const element = target.querySelector(selector);
            if (element) {
                return element.getAttribute('href')
            }
        }

        return "";
    }

    for (const article of articleElements) {
        const href = getAttributeInElement(article, ['a.media__link', 'a.reel__link'])
        const {origin} = window.location;
        const url = href ? (href.includes(origin) ? href : origin +href) : ""

        const title = getTextInElement(article, [".media__title", ".media__content h3"]);
        const description = getTextInElement(article, [".media__summary"]);
        const tag = getTextInElement(article, [".media__tag"]);

        articles.push({url, title, description, tag});
    }

    return articles;
}
