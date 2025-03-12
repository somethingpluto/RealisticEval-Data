/**
 * Removes all punctuation from a given string, converts the string to lowercase,
 * and trims whitespace from both ends.
 *
 * @param {string} str - The string from which to remove punctuation.
 * @returns {string} The cleaned and formatted string.
 */
function removePunctuation(str) {
    // Remove punctuation using a regular expression
    let cleanedStr = str.replace(/[^\w\s]/g, '');
    
    // Convert the string to lowercase
    cleanedStr = cleanedStr.toLowerCase();
    
    // Trim whitespace from both ends
    cleanedStr = cleanedStr.trim();
    
    return cleanedStr;
}
describe('removePunctuation', () => {
    test('removes punctuation from a simple sentence', () => {
        const input = "Hello, world!";
        const expected = "hello world";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('handles a string with no punctuation', () => {
        const input = "Hello world";
        const expected = "hello world";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('converts mixed case letters to lowercase', () => {
        const input = "HeLLo WoRLd!";
        const expected = "hello world";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('removes a variety of punctuation', () => {
        const input = "Life, in a nutshell: eat, sleep, code!";
        const expected = "life in a nutshell eat sleep code";
        expect(removePunctuation(input)).toBe(expected);
    });

    test('trims whitespace from the ends of the string', () => {
        const input = "   What a wonderful world!   ";
        const expected = "what a wonderful world";
        expect(removePunctuation(input)).toBe(expected);
    });
});
