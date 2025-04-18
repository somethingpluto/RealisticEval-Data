/**
 * Checks if a given year is a leap year.
 *
 * @param year The year to check.
 * @return True if the year is a leap year, false otherwise.
 */
function isLeapYear(year: number): boolean {
    // A year is a leap year if:
    // 1. It is divisible by 4 AND
    // 2. It is NOT divisible by 100, OR it is divisible by 400
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}