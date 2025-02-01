/**
 * Detects whether the string is in KEBAB_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in KEBAB_CASE, otherwise false.
 */
function isKebabCase(input) {
    // Check if the string contains any uppercase letters
    if (/[A-Z]/.test(input)) {
        return false;
    }

    // Check if the string contains any spaces
    if (/\s/.test(input)) {
        return false;
    }

    // Check if the string contains any non-alphanumeric characters except for hyphens
    if (/[^a-z0-9\-]/.test(input)) {
        return false;
    }

    // Check if the string contains multiple consecutive hyphens
    if (/\-{2,}/.test(input)) {
        return false;
    }

    // Check if the string starts or ends with a hyphen
    if (input.startsWith('-') || input.endsWith('-')) {
        return false;
    }

    // If all checks pass, the string is in KEBAB_CASE
    return true;
}
describe('isKebabCase', () => {
    test('should return true for a valid kebab-case string', () => {
        expect(isKebabCase('kebab-case')).toBe(true);
    });

    test('should return true for a valid kebab-case string with multiple words', () => {
        expect(isKebabCase('this-is-a-valid-kebab-case')).toBe(true);
    });

    test('should return false for a string with uppercase letters', () => {
        expect(isKebabCase('Kebab-Case')).toBe(false);
    });

    test('should return false for a string with consecutive hyphens', () => {
        expect(isKebabCase('kebab--case')).toBe(false);
    });

    test('should return false for an empty string', () => {
        expect(isKebabCase('')).toBe(false);
    });
});
