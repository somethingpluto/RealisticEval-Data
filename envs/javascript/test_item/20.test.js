/**
 * Transforms the input text by finding and modifying patterns that match the format '(*...*)'.
 * Specifically, it removes any asterisks inside the parentheses while preserving the outer format.
 *
 * @param {string} text - The input text containing patterns to be transformed.
 * @returns {string} - The transformed text with asterisks inside '(*...*)' patterns removed.
 */
function removeInnerAsterisks(text) {
    // Use a regular expression to match the pattern '(*...*)'
    return text.replace(/\*([^*]*)\*/g, (match, p1) => {
        // Remove asterisks inside the parentheses
        return `*${p1.replace(/\*/g, '')}*`;
    });
}
describe('remove_inner_asterisks', () => {
    test('basic case', () => {
        const text = "Hello (*wo*rld*)!";
        const expected = "Hello (*world*)!";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('multiple asterisks', () => {
        const text = "(*he*l*lo*)";
        const expected = "(*hello*)";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('no asterisks inside', () => {
        const text = "(*hello*)";
        const expected = "(*hello*)";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('multiple patterns', () => {
        const text = "(*hi*), (*there*), (*world*)!";
        const expected = "(*hi*), (*there*), (*world*)!";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('no matching pattern', () => {
        const text = "This is a test without matching parentheses.";
        const expected = "This is a test without matching parentheses.";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });
});
