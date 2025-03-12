/**
 * Compress multiple consecutive whitespace characters in a string into a single space.
 *
 * @param {string} inputString - The string to be processed.
 * @returns {string} - The processed string with compressed whitespace.
 */
function compressWhitespace(inputString) {
    // Use a regular expression to replace multiple consecutive whitespace characters with a single space
    return inputString.replace(/\s+/g, ' ');
}
describe('compressWhitespace', () => {
    it('should handle strings with single spaces', () => {
        expect(compressWhitespace("This is a test string.")).toBe("This is a test string.");
    });

    it('should handle strings with multiple spaces', () => {
        expect(compressWhitespace("This    is  a   test   string.")).toBe("This is a test string.");
    });

    it('should handle strings with leading and trailing spaces', () => {
        expect(compressWhitespace("   Leading and trailing spaces   ")).toBe("Leading and trailing spaces");
    });

    it('should handle strings with only spaces', () => {
        expect(compressWhitespace("       ")).toBe("");
    });

    it('should handle empty strings', () => {
        expect(compressWhitespace("")).toBe("");
    });
});
