/**
 * Detects whether the string is in PASCAL_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in PASCAL_CASE, otherwise false.
 */
function isPascalCase(input) {
    // Check if the input is a non-empty string
    if (typeof input !== 'string' || input.length === 0) {
        return false;
    }

    // Check if the first character is uppercase
    if (!/^[A-Z]/.test(input)) {
        return false;
    }

    // Check if the rest of the string is alphanumeric and contains no spaces
    if (!/^[A-Z][a-zA-Z0-9]*$/.test(input)) {
        return false;
    }

    return true;
}
describe('isPascalCase', () => {
    test('should return true for a valid PascalCase string', () => {
        expect(isPascalCase('PascalCase')).toBe(true);
    });

    test('should return true for a valid PascalCase string with multiple words', () => {
        expect(isPascalCase('PascalCaseExample')).toBe(true);
    });

    test('should return false for a string that starts with a lowercase letter', () => {
        expect(isPascalCase('pascalCase')).toBe(false);
    });

    test('should return false for a string with underscores', () => {
        expect(isPascalCase('Pascal_case')).toBe(false);
    });

    test('should return false for a string that is empty', () => {
        expect(isPascalCase('')).toBe(false);
    });
});
