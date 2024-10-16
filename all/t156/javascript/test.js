describe('formatNumber', () => {
    test('should format numbers greater than or equal to 1,000,000 with "M" suffix', () => {
        expect(formatNumber(1500000)).toBe('1.5M');
        expect(formatNumber(1000000)).toBe('1.0M');
    });

    test('should format numbers greater than or equal to 1,000 but less than 1,000,000 with "K" suffix', () => {
        expect(formatNumber(2500)).toBe('2.5K');
        expect(formatNumber(1000)).toBe('1.0K');
    });

    test('should return the number as a string if it is less than 1,000', () => {
        expect(formatNumber(999)).toBe('999');
        expect(formatNumber(500)).toBe('500');
    });

    test('should handle edge cases like exactly 1,000 or 1,000,000', () => {
        expect(formatNumber(1000)).toBe('1.0K');
        expect(formatNumber(1000000)).toBe('1.0M');
    });
});