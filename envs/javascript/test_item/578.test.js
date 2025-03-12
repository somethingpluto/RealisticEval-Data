/**
 * Detects whether the string is in KEBAB_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in KEBAB_CASE, otherwise false.
 */
function isKebabCase(input) {
    // Regular expression to match KEBAB_CASE
    const kebabCaseRegex = /^[a-z]+(-[a-z]+)*$/;
    
    // Test the input string against the regular expression
    return kebabCaseRegex.test(input);
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
