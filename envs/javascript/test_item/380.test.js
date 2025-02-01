/**
 * Calculate the total number of seconds given an array of time periods in the order of
 * days, hours, minutes, and seconds.
 *
 * @param {Array<number>=} time - An array where
 *   time[0] - number of days (optional)
 *   time[1] - number of hours (optional)
 *   time[2] - number of minutes (optional)
 *   time[3] - number of seconds (optional)
 * @returns {number} - The total number of seconds
 *
 * @example
 * calculateTotalSeconds([1, 2, 3, 4]); // returns 93784
 * calculateTotalSeconds([0, 2, 3]); // returns 7380
 */
function calculateTotalSeconds(time = [0, 0, 0, 0]) {
  const secondsInDay = 86400;
  const secondsInHour = 3600;
  const secondsInMinute = 60;

  return (time[0] * secondsInDay) + (time[1] * secondsInHour) + (time[2] * secondsInMinute) + time[3];
}
describe('TestCalculateTotalSeconds', () => {
  describe('test_complete_time', () => {
      it('should correctly calculate total seconds with full values', () => {
          const time = [1, 2, 3, 4];  // 1 day, 2 hours, 3 minutes, 4 seconds
          const expected = 93784;
          const result = calculateTotalSeconds(time);
          expect(result).toBe(expected);
      });
  });

  describe('test_partial_time', () => {
      it('should correctly calculate total seconds with partial values', () => {
          const time = [0, 2, 3];  // 0 days, 2 hours, 3 minutes
          const expected = 7380;
          const result = calculateTotalSeconds(time);
          expect(result).toBe(expected);
      });
  });

  describe('test_seconds_only', () => {
      it('should correctly calculate total seconds with only seconds provided', () => {
          const time = [7200];  // 7200 seconds
          const expected = 7200;
          const result = calculateTotalSeconds(time);
          expect(result).toBe(expected);
      });
  });

  describe('test_no_time', () => {
      it('should correctly calculate total seconds with no time values provided', () => {
          const time = [];
          const expected = 0;
          const result = calculateTotalSeconds(time);
          expect(result).toBe(expected);
      });
  });
});
