/**
 * Returns the current time information including year, month, week of the month, and day of the week.
 * Example output:
 * {
 *     'year': 2024,
 *     'month': 'February',
 *     'week_of_the_month': 5,
 *     'day_of_the_week': 'Thursday'
 * }
 *
 * @param {Date} [testDate] - The date to compute information for, defaults to today's date if not provided.
 * @returns {Object} An object containing the year, month, week of the month, and day of the week.
 */
function getCurrentDateInfo(testDate = new Date()) {
    const months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ];

    const daysOfWeek = [
        'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'
    ];

    const year = testDate.getFullYear();
    const month = months[testDate.getMonth()];
    const dayOfWeek = daysOfWeek[testDate.getDay()];

    // Calculate the week of the month
    const firstDayOfMonth = new Date(testDate.getFullYear(), testDate.getMonth(), 1);
    const firstDayOfWeek = firstDayOfMonth.getDay();
    const dayOfMonth = testDate.getDate();
    const weekOfMonth = Math.ceil((dayOfMonth + firstDayOfWeek) / 7);

    return {
        year: year,
        month: month,
        week_of_the_month: weekOfMonth,
        day_of_the_week: dayOfWeek
    };
}
describe('TestGetCurrentDateInfo', () => {
  describe('test_beginning_of_month', () => {
      it('should return correct info for the beginning of the month', () => {
          const result = get_current_date_info(new Date(2023, 0, 1));
          const expected = {
              'year': 2023,
              'month': 'January',
              'week_of_the_month': 1,
              'day_of_the_week': 'Sunday'
          };
          expect(result).toEqual(expected);
      });
  });

  describe('test_middle_of_month', () => {
      it('should return correct info for the middle of the month', () => {
          const result = get_current_date_info(new Date(2023, 0, 15));
          const expected = {
              'year': 2023,
              'month': 'January',
              'week_of_the_month': 3,
              'day_of_the_week': 'Sunday'
          };
          expect(result).toEqual(expected);
      });
  });

  describe('test_leap_year', () => {
      it('should return correct info for a leap year', () => {
          const result = get_current_date_info(new Date(2024, 1, 29));
          const expected = {
              'year': 2024,
              'month': 'February',
              'week_of_the_month': 5,
              'day_of_the_week': 'Thursday'
          };
          expect(result).toEqual(expected);
      });
  });

  describe('test_change_of_year', () => {
      it('should return correct info for the end of the year', () => {
          const result = get_current_date_info(new Date(2022, 11, 31));
          const expected = {
              'year': 2022,
              'month': 'December',
              'week_of_the_month': 5,
              'day_of_the_week': 'Saturday'
          };
          expect(result).toEqual(expected);
      });
  });
});
