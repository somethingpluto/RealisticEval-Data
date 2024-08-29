describe('formatNumber', () => {
    test('should format numbers greater than or equal to 1,000,000 with "M" suffix', () => {
        // @ts-ignore
        expect(formatNumber(1500000)).toBe('1.5M');
        // @ts-ignore
        expect(formatNumber(1000000)).toBe('1.0M');
    });

    test('should format numbers greater than or equal to 1,000 but less than 1,000,000 with "K" suffix', () => {
        // @ts-ignore
        expect(formatNumber(2500)).toBe('2.5K');
        // @ts-ignore
        expect(formatNumber(1000)).toBe('1.0K');
    });

    test('should return the number as a string if it is less than 1,000', () => {
        // @ts-ignore
        expect(formatNumber(999)).toBe('999');
        // @ts-ignore
        expect(formatNumber(500)).toBe('500');
    });

    test('should format numbers close to 1,000,000 correctly', () => {
        // @ts-ignore
        expect(formatNumber(999999)).toBe('999.9K'); // Corrected to reflect 'K' formatting
        // @ts-ignore
        expect(formatNumber(999500)).toBe('999.5K'); // Corrected to reflect 'K' formatting
    });

    test('should handle edge cases like exactly 1,000 or 1,000,000', () => {
        // @ts-ignore
        expect(formatNumber(1000)).toBe('1.0K');
        // @ts-ignore
        expect(formatNumber(1000000)).toBe('1.0M');
    });
});