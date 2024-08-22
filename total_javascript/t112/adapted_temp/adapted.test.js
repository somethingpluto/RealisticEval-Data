describe('htmlToMDSyntax', () => {
    test('should convert basic HTML tags to Markdown syntax', () => {
        const html = '<h1>Title</h1><p>Paragraph</p><code>code snippet</code>';
        const expected = '# Title\nParagraph\n`code snippet`';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });

    test('should convert ordered list to Markdown syntax', () => {
        const html = '<ol><li>First</li><li>Second</li><li>Third</li></ol>';
        const expected = '1. First\n2. Second\n3. Third';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });

    test('should convert unordered list to Markdown syntax', () => {
        const html = '<ul><li>First</li><li>Second</li><li>Third</li></ul>';
        const expected = '- First\n- Second\n- Third';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });

    test('should handle nested lists correctly such as an ordered list containing an unordered sublist', () => {
        const html = '<ol><li>First<ul><li>Sub First</li></ul></li><li>Second</li></ol>';
        const expected = '1. First\n- Sub First\n\n\n2. Second';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });

    test('should handle mixed content with headings and lists', () => {
        const html = '<h2>Subheading</h2><p>Some text</p><ul><li>Item</li></ul>';
        const expected = '## Subheading\nSome text\n\n- Item';
        const result = htmlToMDSyntax(html);
        expect(result).toBe(expected);
    });
});
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
