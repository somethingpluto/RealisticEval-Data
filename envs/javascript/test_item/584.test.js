/**
 * Detects whether the string is in PASCAL_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in PASCAL_CASE, otherwise false.
 */
function isPascalCase(input) {
    // Check if the input is a string
    if (typeof input !== 'string') {
        return false;
    }

    // Check if the string is in PASCAL_CASE
    // PASCAL_CASE means the first letter is uppercase and the rest are lowercase
    // and there are no spaces or non-alphanumeric characters
    return /^[A-Z][a-z0-9]*$/g.test(input);
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
