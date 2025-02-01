/**
 * Returns the number of days in a given month of a given year.
 *
 * This function accounts for leap years when determining the number of
 * days in February. It throws an error if the month is invalid.
 *
 * @param {number} year The year to check (should be a positive integer).
 * @param {number} month The month to check (1 for January, 12 for December).
 * @return {number} The number of days in the specified month of the specified year.
 * @throws {RangeError} If the month is not between 1 and 12.
 */
function getDaysInMonth(year, month) {
  if (month < 1 || month > 12) {
    throw new RangeError('Month must be between 1 and 12');
  }

  const daysInMonth = [31, isLeapYear(year) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  return daysInMonth[month - 1];
}

function isLeapYear(year) {
  return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}
describe("getDaysInMonth function", () => {
    describe("Regular months", () => {
        test("January", () => {
            expect(getDaysInMonth(2023, 1)).toBe(31);
        });
        test("March", () => {
            expect(getDaysInMonth(2023, 3)).toBe(31);
        });
        test("April", () => {
            expect(getDaysInMonth(2023, 4)).toBe(30);
        });
        test("May", () => {
            expect(getDaysInMonth(2023, 5)).toBe(31);
        });
        test("June", () => {
            expect(getDaysInMonth(2023, 6)).toBe(30);
        });
        test("July", () => {
            expect(getDaysInMonth(2023, 7)).toBe(31);
        });
        test("August", () => {
            expect(getDaysInMonth(2023, 8)).toBe(31);
        });
        test("September", () => {
            expect(getDaysInMonth(2023, 9)).toBe(30);
        });
        test("October", () => {
            expect(getDaysInMonth(2023, 10)).toBe(31);
        });
        test("November", () => {
            expect(getDaysInMonth(2023, 11)).toBe(30);
        });
        test("December", () => {
            expect(getDaysInMonth(2023, 12)).toBe(31);
        });
    });

    describe("February in leap year", () => {
        test("Leap year", () => {
            expect(getDaysInMonth(2024, 2)).toBe(29);
        });
    });

    describe("February in non-leap year", () => {
        test("Non-leap year", () => {
            expect(getDaysInMonth(2023, 2)).toBe(28);
        });
    });
});
