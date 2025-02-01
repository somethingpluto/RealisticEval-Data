/**
 * calculate the date of Good Friday in a given year
 * For example:
 *      input: 2024
 *      output: Fri Mar 29 2024
 * @param year
 */
function calculateGoodFriday(year) {
    // Good Friday is the Friday before Easter Sunday
    // Easter Sunday is the first Sunday after the first full moon after the vernal equinox
    // The following algorithm is based on the Computus algorithm

    // Calculate the golden number
    let goldenNumber = year % 19;

    // Calculate the century
    let century = Math.floor(year / 100);

    // Calculate the correction for the century
    let correctionForCentury = (century - Math.floor(century / 4) - Math.floor((8 * century + 13) / 25) + 19 * goldenNumber) % 30;

    // Calculate the epact
    let epact = correctionForCentury + Math.floor((21 * goldenNumber + correctionForCentury) / 11);

    // Calculate the day of the month
    let dayOfMonth = (epact + Math.floor((29578 - (year * 365 + century * 367 + Math.floor((3 * (century + 1)) / 4) + Math.floor((5 * year) / 4) - 329)) / 153)) % 7;

    // Calculate the date of Easter Sunday
    let easterSunday = new Date(year, 2, (22 + dayOfMonth));

    // Calculate the date of Good Friday
    let goodFriday = new Date(easterSunday.getTime() - (3 * 24 * 60 * 60 * 1000));

    // Return the date of Good Friday in the format "Day Mon DD YYYY"
    return goodFriday.toDateString();
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
