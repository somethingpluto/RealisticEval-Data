/**
 * Gets the line number in the content at the specified index.
 *
 * @param {string} content - The string content to check.
 * @param {number} index - The character index to find the line number for.
 * @returns {number} - The line number corresponding to the given index.
 */
function getLineNumber(content, index) {
    // Use a regular expression to count the number of newline characters before the index
    return (content.slice(0, index).match(/\n/g) || []).length + 1;
}
describe('getLineNumber', () => {
    test('returns 1 for the first character', () => {
        expect(getLineNumber("Line 1\nLine 2\nLine 3", 0)).toBe(1);
    });

    test('returns 1 for the last character of the first line', () => {
        expect(getLineNumber("Line 1\nLine 2\nLine 3", 5)).toBe(1);
    });

    test('returns 3 for the last character of the third line', () => {
        expect(getLineNumber("Line 1\nLine 2\nLine 3", 18)).toBe(3);
    });

    test('returns 1 for a single line string', () => {
        expect(getLineNumber("Single line string", 0)).toBe(1);
    });

    test('returns 3 for an index within a multiline string with trailing newlines', () => {
        expect(getLineNumber("Line 1\nLine 2\nLine 3\n\n", 15)).toBe(3);
    });
});
