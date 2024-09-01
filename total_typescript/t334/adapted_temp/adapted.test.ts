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
function calculateGoodFriday(year: number): Date {
    // Gauss's Algorithm to determine the date of Easter Sunday
    const a = year % 19;
    const b = Math.floor(year / 100);
    const c = year % 100;
    const d = Math.floor(b / 4);
    const e = b % 4;
    const f = Math.floor((b + 8) / 25);
    const g = Math.floor((b - f + 1) / 3);
    const h = (19 * a + b - d - g + 15) % 30;
    const i = Math.floor(c / 4);
    const k = c % 4;
    const l = (32 + 2 * e + 2 * i - h - k) % 7;
    const m = Math.floor((a + 11 * h + 22 * l) / 451);
    const month = Math.floor((h + l - 7 * m + 114) / 31);
    const day = ((h + l - 7 * m + 114) % 31) + 1;

    // Easter Sunday Date
    const easterSunday = new Date(year, month - 1, day);

    // Good Friday is 2 days before Easter Sunday
    const goodFriday = new Date(easterSunday.getTime());
    goodFriday.setDate(goodFriday.getDate() - 2);

    return goodFriday;
}