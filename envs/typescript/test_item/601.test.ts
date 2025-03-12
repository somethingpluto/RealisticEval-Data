/**
 * Counts the number of words in a given string.
 *
 * A word is defined as a sequence of characters separated by whitespace.
 * This function handles leading and trailing whitespace, as well as
 * multiple spaces between words.
 *
 * @param {string} str The input string in which words are to be counted.
 * @return {number} The count of words in the input string.
 */
function countWords(str: string): number {
    return str.trim().split(/\s+/).filter(Boolean).length;
}
describe('Count words in various strings', () => {
    test('Empty string', () => {
        expect(countWords("")).toBe(0);
    });

    test('String with only spaces', () => {
        expect(countWords("     ")).toBe(0);
    });

    test('Single word', () => {
        expect(countWords("Hello")).toBe(1);
    });

    test('Multiple words with single spaces', () => {
        expect(countWords("This is a test string")).toBe(5);
    });

    test('Multiple spaces between words', () => {
        expect(countWords("This    is   a   test   string")).toBe(5);
    });

    test('Leading and trailing spaces', () => {
        expect(countWords("   Hello world!   ")).toBe(2);
    });
});
