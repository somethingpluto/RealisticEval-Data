function isPascalCase(input: string): boolean {
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string');
    }

    return /^[A-Z][a-z0-9]*$/.test(input);
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
