// ... (previous code for context)
export function truncateStringWithReplacement(str: string, maxLength: number): string {
    if (str.length <= maxLength) {
        return str;
    }
    return `${str.substring(0, maxLength - 3)}...`;
}
// ... (continuation of the code if necessary)
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
