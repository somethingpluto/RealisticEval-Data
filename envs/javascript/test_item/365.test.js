/**
 * Calculates the day of the week for a given date.
 *
 * @param {number} year The year of the date (e.g., 2024).
 * @param {number} month The month of the date (1 = January, 2 = February, ..., 12 = December).
 * @param {number} day The day of the month (1 to 31, depending on the month).
 * 
 * @return {number} An integer representing the day of the week:
 *         - 1 for Monday
 *         - 2 for Tuesday
 *         - 3 for Wednesday
 *         - 4 for Thursday
 *         - 5 for Friday
 *         - 6 for Saturday
 *         - 7 for Sunday
 */
function dayOfWeek(year, month, day) {
    // Adjust month and year for Zeller's Congruence
    if (month < 3) {
        month += 12;
        year -= 1;
    }

    // Zeller's Congruence formula
    const q = day;
    const m = month;
    const K = year % 100;
    const J = Math.floor(year / 100);

    const h = (q + Math.floor((13 * (m + 1)) / 5) + K + Math.floor(K / 4) + Math.floor(J / 4) + 5 * J) % 7;

    // Convert Zeller's result to ISO week day (1 = Monday, ..., 7 = Sunday)
    const d = ((h + 5) % 7) + 1;

    return d;
}
describe("Day of Week Calculation", () => {
    test("January 1, 2024 is a Monday", () => {
        expect(dayOfWeek(2024, 1, 1)).toBe(1);
    });

    test("August 29, 2023 is a Tuesday", () => {
        expect(dayOfWeek(2023, 8, 29)).toBe(2);
    });

    test("December 25, 2022 is a Sunday", () => {
        expect(dayOfWeek(2022, 12, 25)).toBe(7);
    });

    test("November 9, 1989 is a Thursday", () => {
        expect(dayOfWeek(1989, 11, 9)).toBe(4);
    });

    test("February 29, 2000 is a Tuesday", () => {
        expect(dayOfWeek(2000, 2, 29)).toBe(2);
    });
});
