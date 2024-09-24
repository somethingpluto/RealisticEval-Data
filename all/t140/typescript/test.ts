describe('getTimeSinceBornUntilNow', () => {
    beforeAll(() => {
        jest.useFakeTimers().setSystemTime(new Date('2024-08-23T15:45:00'));
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    test('should return the correct difference for a typical birth date', () => {
        const birthDate = new Date('1990-05-15T10:30:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([34, 3, 8, 5, 15]); // Example output: 34 years, 3 months, 8 days, 5 hours, 15 minutes
    });

    test('should return the correct difference for a recent birth date', () => {
        const birthDate = new Date('2024-08-20T12:00:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([0, 0, 3, 3, 45]); // 3 days, 3 hours, 45 minutes
    });
    test('should return negative values for a birth date in the future', () => {
        const birthDate = new Date('2025-01-01T00:00:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([-1, 4, 7, 15, 45]); // Negative years, months, days, etc.
    });

    test('should handle edge cases at the end of the year', () => {
        const birthDate = new Date('2023-12-31T23:59:00');
        const result = getTimeSinceBornUntilNow(birthDate);
        expect(result).toEqual([0, 7, 22, 15, 46]); // 7 months, 22 days, 15 hours, 46 minutes
    });
});