/**
 * Detects whether the string is in CAMEL_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in CAMEL_CASE, otherwise false.
 */
function isCamelCase(input) {
    // Check if the input is a non-empty string
    if (typeof input !== 'string' || input.length === 0) {
        return false;
    }

    // Check if the string starts with a lowercase letter
    if (!/^[a-z]/.test(input)) {
        return false;
    }

    // Check if the string contains only alphanumeric characters
    if (!/^[a-zA-Z0-9]+$/.test(input)) {
        return false;
    }

    // Check if the string has no consecutive uppercase letters
    if (/[A-Z]{2,}/.test(input)) {
        return false;
    }

    // Check if the string has at least one uppercase letter (indicating camelCase)
    if (!/[A-Z]/.test(input)) {
        return false;
    }

    return true;
}
describe('isCamelCase', () => {
    test('should return true for a valid camelCase string', () => {
        expect(isCamelCase('camelCase')).toBe(true);
    });

    test('should return true for a valid camelCase string with multiple words', () => {
        expect(isCamelCase('camelCaseExample')).toBe(true);
    });

    test('should return false for a string that starts with an uppercase letter', () => {
        expect(isCamelCase('CamelCase')).toBe(false);
    });

    test('should return false for a string with underscores', () => {
        expect(isCamelCase('camel_case')).toBe(false);
    });

    test('should return false for an empty string', () => {
        expect(isCamelCase('')).toBe(false);
    });
});
