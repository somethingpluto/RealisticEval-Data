describe('Day of Week Calculation', () => {
    test('January 1, 2024 is a Monday', () => {
        expect(dayOfWeek(2024, 1, 1)).toBe(1);
    });

    test('August 29, 2023 is a Tuesday', () => {
        expect(dayOfWeek(2023, 8, 29)).toBe(2);
    });

    test('December 25, 2022 is a Sunday', () => {
        expect(dayOfWeek(2022, 12, 25)).toBe(7);
    });

    test('November 9, 1989 is a Thursday', () => {
        expect(dayOfWeek(1989, 11, 9)).toBe(4);
    });

    test('February 29, 2000 is a Tuesday', () => {
        expect(dayOfWeek(2000, 2, 29)).toBe(2);
    });
});