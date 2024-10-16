describe('getDaysInMonth', () => {
    test('Leap year February', () => {
        expect(getDaysInMonth(2024, 2)).toBe(29); // 2024 is a leap year
    });

    test('Non-leap year February', () => {
        expect(getDaysInMonth(2023, 2)).toBe(28); // 2023 is not a leap year
    });

    test('Month with 31 days', () => {
        expect(getDaysInMonth(2023, 1)).toBe(31); // January has 31 days
        expect(getDaysInMonth(2023, 7)).toBe(31); // July has 31 days
    });

    test('Month with 30 days', () => {
        expect(getDaysInMonth(2023, 4)).toBe(30); // April has 30 days
        expect(getDaysInMonth(2023, 11)).toBe(30); // November has 30 days
    });

    test('Invalid month', () => {
        expect(() => getDaysInMonth(2023, 0)).toThrowError('Month must be between 1 and 12.'); // Month less than 1
        expect(() => getDaysInMonth(2023, 13)).toThrowError('Month must be between 1 and 12.'); // Month greater than 12
    });
});