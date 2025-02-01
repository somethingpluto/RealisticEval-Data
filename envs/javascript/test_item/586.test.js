/**
 * Detects whether the string is in SNAKE_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in SNAKE_CASE, otherwise false.
 */
function isSnakeCase(input) {
    // Check if the input is a string
    if (typeof input !== 'string') {
        return false;
    }

    // Check if the string contains any uppercase letters
    if (/[A-Z]/.test(input)) {
        return false;
    }

    // Check if the string contains underscores and only lowercase letters
    if (/[^a-z_]/.test(input) || input[0] === '_' || input[input.length - 1] === '_') {
        return false;
    }

    // Check if the string contains consecutive underscores
    if (/_{2,}/.test(input)) {
        return false;
    }

    // If all checks pass, the string is in SNAKE_CASE
    return true;
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
