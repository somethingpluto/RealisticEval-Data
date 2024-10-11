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