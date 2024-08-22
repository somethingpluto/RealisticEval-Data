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
function htmlToMDSyntax(html) { // accounts for an edge case where chatgpt produces both an ordered list and an unordered list when exporting
    let newh =  html
        .replaceAll(`<code>`, '\`')
        .replaceAll(`</code>`, '\`')
        .replaceAll(`<p>`, '\n')
        .replaceAll(`</p>`, '\n')
        .replaceAll(`<h1>`, '# ')
        .replaceAll(`</h1>`, '')
        .replaceAll(`<h2>`, '## ')
        .replaceAll(`</h2>`, '')
        .replaceAll(`<h3>`, '### ')
        .replaceAll(`</h3>`, '');

    let isOrderedList = html.includes('<ol>');
    let isUnorderedList = html.includes('<ul>');

    if (isOrderedList){
        newh = newh
            .replaceAll(`<ol>`, `<ol class="ordered-list">`)
            .replaceAll(`</ol>`, `</ol>`);

        let parser = new DOMParser();
        let doc = parser.parseFromString(newh, 'text/html');
        let orderedListItems = doc.querySelectorAll('.ordered-list li');
        for (let i = 0; i < orderedListItems.length; i++) {
            orderedListItems[i].innerHTML = `${i + 1}. ` + orderedListItems[i].innerHTML;
        }
        newh = doc.body.innerHTML
            .replaceAll(`<ol class="ordered-list">`, "\n")
            .replaceAll(`</ol>`, "\n")
            .replaceAll(`</li>`, "\n")
    }
    if (isUnorderedList){
        newh = newh
            .replaceAll(`<ul>`, `<ul class="unordered-list">`)
            .replaceAll(`</ul>`, `</ul>`);

        let parser = new DOMParser();
        let doc = parser.parseFromString(newh, 'text/html');
        let unorderedListItems = doc.querySelectorAll('.unordered-list li');
        for (let i = 0; i < unorderedListItems.length; i++) {
            unorderedListItems[i].innerHTML = `- ` + unorderedListItems[i].innerHTML;
        }
        newh = doc.body.innerHTML
            .replaceAll(`<ul class="unordered-list">`, "\n")
            .replaceAll(`</ul>`, "\n")
            .replaceAll(`</li>`, "\n")
    }
    newh = newh.replaceAll(`<li>`, "")

    return newh
}