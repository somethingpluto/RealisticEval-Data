/**
 * Truncate a string to the specified length, replacing the excess part with an ellipsis.
 *
 * @param {string} str - The string to truncate.
 * @param {number} maxLength - The maximum length of the resulting string.
 * @returns {string} - The truncated string with ellipsis if applicable.
 */
function truncateStringWithReplacement(str, maxLength) {
    if (str.length <= maxLength) {
        return str;
    }
    const ellipsis = '...';
    const truncatedLength = maxLength - ellipsis.length;
    if (truncatedLength <= 0) {
        return ellipsis;
    }
    return str.slice(0, truncatedLength) + ellipsis;
}
describe('truncateStringWithReplacement', () => {
    test('should return the original string if it is shorter than maxLength', () => {
        const result = truncateStringWithReplacement('Hello World', 20);
        expect(result).toBe('Hello World');
    });

    test('should truncate the string and replace the excess with ellipsis when longer than maxLength', () => {
        const result = truncateStringWithReplacement('This is a long string that needs to be truncated.', 20);
        expect(result).toBe('This is a long str...');
    });

    test('should truncate the string at maxLength and add ellipsis', () => {
        const result = truncateStringWithReplacement('Short string', 10);
        expect(result).toBe('Short str...');
    });

    test('should handle empty string correctly', () => {
        const result = truncateStringWithReplacement('', 10);
        expect(result).toBe('');
    });

    test('should return the original string when maxLength is equal to string length', () => {
        const result = truncateStringWithReplacement('Exact length', 12);
        expect(result).toBe('Exact length');
    });

    test('should replace excess part with ellipsis in a string with special characters', () => {
        const result = truncateStringWithReplacement('This string has special characters: !@#$%^&*()', 30);
        expect(result).toBe('This string has special c...');
    });

    test('should return ellipsis only when the maxLength is 0', () => {
        const result = truncateStringWithReplacement('Hello, world!', 0);
        expect(result).toBe('...');
    });
});
