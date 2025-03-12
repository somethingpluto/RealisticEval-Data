/**
 * Returns the number of days in a given month of a specific year.
 *
 * This function accounts for leap years when calculating the number of days in February.
 *
 * @param {number} year - The year for which to get the number of days in the month.
 * @param {number} month - The month for which to get the number of days (1-12).
 * @return {number} The number of days in the specified month of the specified year.
 */
function getDaysInMonth(year, month) {
    // Adjust month to be 0-indexed for JavaScript's Date object
    month -= 1;

    // Create a new Date object for the first day of the next month
    const nextMonth = new Date(year, month + 1, 1);

    // Subtract one day to get the last day of the specified month
    nextMonth.setDate(nextMonth.getDate() - 1);

    // Return the day of the month (which is the number of days in the month)
    return nextMonth.getDate();
}
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
