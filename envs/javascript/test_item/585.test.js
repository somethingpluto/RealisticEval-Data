/**
 * Detects whether the string is in CAMEL_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in CAMEL_CASE, otherwise false.
 */
function isCamelCase(input) {
    // Check if the input is a string
    if (typeof input !== 'string') {
        return false;
    }

    // Check if the string starts with a lowercase letter
    if (input[0] === input[0].toLowerCase()) {
        return false;
    }

    // Check if the string contains any uppercase letters followed by lowercase letters
    for (let i = 1; i < input.length; i++) {
        if (input[i] === input[i].toUpperCase() && input[i + 1] === input[i + 1].toLowerCase()) {
            continue;
        } else if (input[i] === input[i].toLowerCase() || input[i] === input[i].toUpperCase()) {
            continue;
        } else {
            return false;
        }
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
