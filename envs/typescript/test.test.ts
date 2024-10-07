/**
 * Detects whether the string is in SNAKE_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in SNAKE_CASE, otherwise false.
 */
function isSnakeCase(input: string): boolean {
    return /^[A-Z]+(_[A-Z]+)*$/.test(input);
}
describe('isSnakeCase', () => {
    test('should return true for a valid snake_case string', () => {
        expect(isSnakeCase('snake_case')).toBe(true);
    });

    test('should return true for a valid snake_case string with multiple words', () => {
        expect(isSnakeCase('snake_case_example')).toBe(true);
    });

    test('should return false for a string that starts with an uppercase letter', () => {
        expect(isSnakeCase('Snake_Case')).toBe(false);
    });

    test('should return false for a string with mixed case letters', () => {
        expect(isSnakeCase('snakeCASE')).toBe(false);
    });

    test('should return false for a string with numbers', () => {
        expect(isSnakeCase('snake_case_123')).toBe(false);
    });

    test('should return false for an empty string', () => {
        expect(isSnakeCase('')).toBe(false);
    });
});
