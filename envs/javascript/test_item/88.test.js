/**
 * Parse a cron expression and determine whether it is between 2 a.m. and 4 a.m.
 * @param {string} cronExpression - The cron expression to parse.
 * @returns {boolean} - True if the cron expression is between 2 a.m. and 4 a.m., false otherwise.
 */
function isCronBetween2And4AM(cronExpression) {
  // Split the cron expression into its components
  const cronParts = cronExpression.split(' ');

  // Check if the cron expression has the correct number of fields
  if (cronParts.length !== 5) {
    throw new Error('Invalid cron expression format');
  }

  // Extract the hour part of the cron expression
  const hour = parseInt(cronParts[1], 10);

  // Check if the hour is between 2 and 4 (inclusive)
  return hour >= 2 && hour <= 4;
}
describe('isCronBetween2And4AM', () => {
    test('should return true for specific hours 2, 3, and 4', () => {
        expect(isCronBetween2And4AM('0 2,3,4 * * *')).toBe(true);
    });

    test('should return false for range that includes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 1-5 * * *')).toBe(false);
    });

    test('should return false for range that excludes 2 to 4 a.m.', () => {
        expect(isCronBetween2And4AM('0 0-1,5-23 * * *')).toBe(false);
    });

    test('should return true for wildcard in hour field', () => {
        expect(isCronBetween2And4AM('0 * * * *')).toBe(false);
    });
});

