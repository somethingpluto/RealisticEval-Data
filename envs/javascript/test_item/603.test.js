/**
 * Checks if a given year is a leap year.
 *
 * @param {number} year - The year to check.
 * @return {boolean} True if the year is a leap year, false otherwise.
 */
function isLeapYear(year) {
    if (year % 4 === 0) {
        if (year % 100 === 0) {
            if (year % 400 === 0) {
                return true;
            } else {
                return false;
            }
        } else {
            return true;
        }
    } else {
        return false;
    }
}
describe("Leap Year Test Cases", () => {
    test("Divisible by 4 but not by 100", () => {
        // Years that are leap years
        expect(isLeapYear(2024)).toBe(true); // 2024 is a leap year
        expect(isLeapYear(2000)).toBe(true); // 2000 is a leap year (divisible by 400)
        expect(isLeapYear(1996)).toBe(true); // 1996 is a leap year
        expect(isLeapYear(2004)).toBe(true); // 2004 is a leap year
    });

    test("Divisible by 100 but not by 400", () => {
        // Years that are not leap years
        expect(isLeapYear(1900)).toBe(false); // 1900 is not a leap year
        expect(isLeapYear(2100)).toBe(false); // 2100 is not a leap year
        expect(isLeapYear(1800)).toBe(false); // 1800 is not a leap year
    });

    test("Divisible by 400", () => {
        // Years that are leap years
        expect(isLeapYear(2400)).toBe(true); // 2400 is a leap year
        expect(isLeapYear(1600)).toBe(true); // 1600 is a leap year
    });

    test("Normal years", () => {
        // Years that are normal years
        expect(isLeapYear(1997)).toBe(false); // 1997 is not a leap year
        expect(isLeapYear(1998)).toBe(false); // 1998 is not a leap year
        expect(isLeapYear(1999)).toBe(false); // 1999 is not a leap year
    });
});
