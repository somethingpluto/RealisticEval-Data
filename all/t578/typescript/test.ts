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