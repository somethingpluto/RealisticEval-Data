/**
 * Calculate the date of Good Friday in a given year
 * @param {number} year - The year to calculate Good Friday for
 * @returns {Date} - The date of Good Friday in the given year
 */
function calculateGoodFriday(year) {
    // Calculate the date of Easter Sunday using the Meeus/Jones/Butcher algorithm
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
    const month = Math.floor((h + l - 7 * m + 114) / 31) - 1; // Months are 0-based in JavaScript Date
    const day = ((h + l - 7 * m + 114) % 31) + 1;

    // Create a Date object for Easter Sunday
    const easterSunday = new Date(year, month, day);

    // Subtract 2 days to get Good Friday
    easterSunday.setDate(easterSunday.getDate() - 2);

    return easterSunday;
}
describe('calculateGoodFriday', () => {
    it('should correctly calculate Good Friday for 2024', () => {
        const result = calculateGoodFriday(2024);
        expect(result.toDateString()).toBe('Fri Mar 29 2024');
    });

    it('should correctly calculate Good Friday for 2021', () => {
        const result = calculateGoodFriday(2021);
        expect(result.toDateString()).toBe('Fri Apr 02 2021');
    });

    it('should correctly calculate Good Friday for 2000', () => {
        const result = calculateGoodFriday(2000);
        expect(result.toDateString()).toBe('Fri Apr 21 2000');
    });

    it('should correctly calculate Good Friday for 2019', () => {
        const result = calculateGoodFriday(2019);
        expect(result.toDateString()).toBe('Fri Apr 19 2019');
    });

    it('should correctly calculate Good Friday for 1999', () => {
        const result = calculateGoodFriday(1999);
        expect(result.toDateString()).toBe('Fri Apr 02 1999');
    });

    it('should correctly calculate Good Friday for 1981', () => {
        const result = calculateGoodFriday(1981);
        expect(result.toDateString()).toBe('Fri Apr 17 1981');
    });

    it('should correctly calculate Good Friday for 1954', () => {
        const result = calculateGoodFriday(1954);
        expect(result.toDateString()).toBe('Fri Apr 16 1954');
    });
});
