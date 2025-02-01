/**
 * Convert a time duration string in the format 'XhYminZs' to milliseconds.
 *
 * This function takes a string representing a time duration, where hours, minutes, and seconds
 * are optionally provided, and converts this duration into the equivalent number of milliseconds.
 *
 * @param {string} timeStr - A string representing the time duration, e.g., '1h20min30s'.
 * @returns {number | null} - The equivalent duration in milliseconds, or null if the input is invalid.
 */
function convertHmsToMilliseconds(timeStr) {
    const regex = /(\d+h)?(\d+min)?(\d+s)?/;
    const match = timeStr.match(regex);

    if (!match) {
        return null;
    }

    let hours = 0;
    let minutes = 0;
    let seconds = 0;

    if (match[1]) {
        hours = parseInt(match[1], 10);
    }
    if (match[2]) {
        minutes = parseInt(match[2], 10);
    }
    if (match[3]) {
        seconds = parseInt(match[3], 10);
    }

    const milliseconds = hours * 3600000 + minutes * 60000 + seconds * 1000;
    return milliseconds;
}
describe('TestConvertHmsToMilliseconds', () => {
  test('test_basic_conversion', () => {
      expect(convertHmsToMilliseconds("1h20min30s")).toBe(4830000);
  });

  test('test_no_hours_or_minutes', () => {
      expect(convertHmsToMilliseconds("30s")).toBe(30000);
  });

  test('test_invalid_format', () => {
      expect(convertHmsToMilliseconds("1hour20minutes")).toBeNull();
  });

  test('test_edge_case_max_one_day', () => {
      expect(convertHmsToMilliseconds("23h59min59s")).toBe(86399000);
  });

  test('test_exceeding_one_day', () => {
      expect(convertHmsToMilliseconds("24h1min")).toBe(86460000);
  });
});
