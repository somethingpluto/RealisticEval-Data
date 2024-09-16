describe('calculateGoodFriday', () => {
    test('Good Friday calculation for a typical year (2023)', () => {
        const result = calculateGoodFriday(2023);
        expect(result.toDateString()).toBe('Fri Apr 07 2023');
    });

    test('Good Friday calculation for a leap year (2024)', () => {
        const result = calculateGoodFriday(2024);
        expect(result.toDateString()).toBe('Fri Mar 29 2024');
    });

    test('Good Friday calculation for an early Easter (2016)', () => {
        const result = calculateGoodFriday(2016);
        expect(result.toDateString()).toBe('Fri Mar 25 2016');
    });

    test('Good Friday calculation for a late Easter (2019)', () => {
        const result = calculateGoodFriday(2019);
        expect(result.toDateString()).toBe('Fri Apr 19 2019');
    });

    test('Good Friday calculation for a boundary year (2000)', () => {
        const result = calculateGoodFriday(2000);
        expect(result.toDateString()).toBe('Fri Apr 21 2000');
    });
});