/**
 * The HTML text content is converted into Markdown format, and the ordered and unordered lists are specially processed
 *
 * @param {string} html - The HTML string to be converted.
 * @returns {string} - The converted Markdown string.
 */
const { JSDOM } = require('jsdom');

function htmlToMDSyntax(html) {
    let newh = html
        .replaceAll('<code>', '`')
        .replaceAll('</code>', '`')
        .replaceAll('<p>', '\n')
        .replaceAll('</p>', '\n')
        .replaceAll('<h1>', '# ')
        .replaceAll('</h1>', '')
        .replaceAll('<h2>', '## ')
        .replaceAll('</h2>', '')
        .replaceAll('<h3>', '### ')
        .replaceAll('</h3>', '');

    let isOrderedList = html.includes('<ol>');
    let isUnorderedList = html.includes('<ul>');

    if (isOrderedList) {
        newh = newh
            .replaceAll('<ol>', '<ol class="ordered-list">')
            .replaceAll('</ol>', '</ol>');

        const dom = new JSDOM(newh);
        const doc = dom.window.document;
        const orderedListItems = doc.querySelectorAll('.ordered-list li');

        let counter = 1;
        orderedListItems.forEach(item => {
            // If the item is part of a nested list, skip increasing the top-level counter
            if (item.parentElement.className === 'ordered-list') {
                item.innerHTML = `${counter++}. ` + item.innerHTML.trim();
            }
        });

        newh = doc.body.innerHTML
            .replaceAll('<ol class="ordered-list">', "\n")
            .replaceAll('</ol>', "")
            .replaceAll('</li>', "\n");
    }

    if (isUnorderedList) {
        newh = newh
            .replaceAll('<ul>', '<ul class="unordered-list">')
            .replaceAll('</ul>', '</ul>');

        const dom = new JSDOM(newh);
        const doc = dom.window.document;
        const unorderedListItems = doc.querySelectorAll('.unordered-list li');

        unorderedListItems.forEach(item => {
            item.innerHTML = `- ` + item.innerHTML.trim();
        });

        newh = doc.body.innerHTML
            .replaceAll('<ul class="unordered-list">', "\n")
            .replaceAll('</ul>', "")
            .replaceAll('</li>', "\n");
    }

    newh = newh.replaceAll('<li>', '');

    return newh.trim();
}
