describe('isCronBetween2And4AM', () => {
    test('should return true for specific hours 2, 3, and 4', () => {
        expect(isCronBetween2And4AM('0 2,3,4 * * *')).toBe(true);
    });

    test('should return true for range that includes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 1-5 * * *')).toBe(true);
    });

    test('should return false for range that excludes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 0-1,5-23 * * *')).toBe(false);
    });

    test('should return true for wildcard in hour field', () => {
        expect(isCronBetween2And4AM('0 * * * *')).toBe(true);
    });

    test('should throw an error for invalid cron expressions', () => {
        expect(() => {
            isCronBetween2And4AM('invalid input');
        }).toThrow('Invalid cron expression');
    });
});