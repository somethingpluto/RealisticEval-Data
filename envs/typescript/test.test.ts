/**
 * Decodes HTML entities in a given HTML string.
 * @param {string} htmlString - The HTML string containing entities to decode.
 * @returns {string} The decoded string with HTML entities converted back to their original characters.
 */
function replaceHtmlEntities(htmlString: string): string {
    if (typeof htmlString !== 'string') {
        throw new TypeError('Input must be a string.');
    }

    // Use a DOMParser to parse the string as HTML
    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlString, 'text/html');

    // Return the text content, effectively decoding HTML entities
    return doc.documentElement.textContent || "";
}
describe('replaceHtmlEntities', () => {
    test('decodes standard HTML entities', () => {
        const input: string = 'The &amp; symbol should become an &quot;and&quot; sign.';
        const expected: string = 'The & symbol should become an "and" sign.';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('returns empty string for empty input', () => {
        const input: string = '';
        const expected: string = '';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('decodes multiple different entities in one string', () => {
        const input: string = '&lt;div&gt;Hello &amp; Welcome to the &apos;World&apos;!&lt;/div&gt;';
        const expected: string = '<div>Hello & Welcome to the \'World\'!</div>';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('handles strings with no entities', () => {
        const input: string = 'Just a normal string without entities.';
        const expected: string = 'Just a normal string without entities.';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });
});
