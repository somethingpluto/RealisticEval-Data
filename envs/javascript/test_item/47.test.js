/**
 * Calculates the date of the nth occurrence of a specific weekday (k) in a given month (m) and year (y).
 * If the nth occurrence does not exist within the month, it returns the last occurrence of that weekday in the month.
 * This function extends the capability to handle edge cases where the nth weekday might not be present,
 * by providing the closest previous weekday in such cases.
 * 
 * @param {number} y - The year for which the date is to be calculated.
 * @param {number} m - The month for which the date is to be calculated, where January is 1 and December is 12.
 * @param {number} n - The nth occurrence of the weekday within the month. For example, 1 for the first occurrence, 2 for the second, etc.
 * @param {number} k - The weekday, where Monday is 1 and Sunday is 7.
 * @returns {Date} The calculated date of the nth occurrence of the weekday in the given month and year.
 *                If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
 */
function findNthWeekdayOfSpecificYear(y, m, n, k) {
    // Create a new date object for the first day of the given month and year
    let date = new Date(y, m - 1, 1);

    // Adjust the date to the first occurrence of the desired weekday (k)
    while (date.getDay() !== k) {
        date.setDate(date.getDate() + 1);
    }

    // Calculate the nth occurrence of the weekday
    date.setDate(date.getDate() + (n - 1) * 7);

    // Check if the calculated date is still within the same month
    if (date.getMonth() !== m - 1) {
        // If not, find the last occurrence of the weekday in the month
        date.setDate(date.getDate() - 7);
    }

    return date;
}
describe('TestFindNthWeekdayOfSpecificYear', () => {
  describe('Regular Occurrence', () => {
      it('should return the 2nd Monday of May 2023', () => {
          const result = findNthWeekdayOfSpecificYear(2023, 5, 2, 0); // Monday is 0
          const expected = new Date(2023, 4, 8); // Note: Months are 0-indexed in JavaScript
          expect(result).toEqual(expected);
      });
  });

  describe('Last Occurrence', () => {
      it('should return the last Monday of May 2023', () => {
          const result = findNthWeekdayOfSpecificYear(2023, 5, 5, 0); // Monday is 0
          const expected = new Date(2023, 4, 29); // Note: Months are 0-indexed in JavaScript
          expect(result).toEqual(expected);
      });
  });

  describe('First Day is Weekday', () => {
      it('should return the 1st Tuesday of August 2023', () => {
          const result = findNthWeekdayOfSpecificYear(2023, 8, 1, 1); // Tuesday is 1
          const expected = new Date(2023, 7, 1); // Note: Months are 0-indexed in JavaScript
          expect(result).toEqual(expected);
      });
  });

  describe('Edge Year Transition', () => {
      it('should return the 1st Friday of December 2023', () => {
          const result = findNthWeekdayOfSpecificYear(2023, 12, 1, 4); // Friday is 4
          const expected = new Date(2023, 11, 1); // Note: Months are 0-indexed in JavaScript
          expect(result).toEqual(expected);
      });
  });
});
