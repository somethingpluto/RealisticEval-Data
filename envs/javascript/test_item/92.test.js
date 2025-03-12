/**
 * @jest-environment jsdom
 */const { JSDOM } = require('jsdom');
const dom = new JSDOM();
const { document } = dom.window;

/**
 * Decodes HTML entities in a given HTML string.
 * @param {string} htmlString - The HTML string containing entities to decode.
 * @returns {string} The decoded string with HTML entities converted back to their original characters.
 */
function replaceHtmlEntities(htmlString) {
    const tempElement = document.createElement('div');
    tempElement.innerHTML = htmlString;
    return tempElement.textContent || tempElement.innerText || '';
}
describe('replaceHtmlEntities', () => {
    test('decodes standard HTML entities', () => {
        const input = 'The &amp; symbol should become an &quot;and&quot; sign.';
        const expected = 'The & symbol should become an "and" sign.';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('returns empty string for empty input', () => {
        const input = '';
        const expected = '';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });


    test('decodes multiple different entities in one string', () => {
        const input = '&lt;div&gt;Hello &amp; Welcome to the &apos;World&apos;!&lt;/div&gt;';
        const expected = '<div>Hello & Welcome to the \'World\'!</div>';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('handles strings with no entities', () => {
        const input = 'Just a normal string without entities.';
        const expected = 'Just a normal string without entities.';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });
});
