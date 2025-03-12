function isCamelCase(input: string): boolean {
    if (typeof input !== 'string') {
        throw new TypeError('Input must be a string');
    }

    return /^[a-z]+([A-Z][a-z]+)*$/.test(input);
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
