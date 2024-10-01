describe('abbreviateNumber', () => {
    test('should return the same number for values less than 1000', () => {
        expect(abbreviateNumber(999)).toBe('999');
    });

    test('should return "1k" for 1000', () => {
        expect(abbreviateNumber(1000)).toBe('1k');
    });

    test('should return "1.5k" for 1500', () => {
        expect(abbreviateNumber(1500)).toBe('1.5k');
    });

    test('should return "1M" for 1 million', () => {
        expect(abbreviateNumber(1000000)).toBe('1M');
    });

    test('should return "25M" for 25 million', () => {
        expect(abbreviateNumber(25000000)).toBe('25M');
    });

    test('should return "1B" for 1 billion', () => {
        expect(abbreviateNumber(1000000000)).toBe('1B');
    });

    test('should return "1.2T" for 1.2 trillion', () => {
        expect(abbreviateNumber(1234567890123)).toBe('1.2T');
    });
});