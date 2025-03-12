/**
 * Converts a time duration string into a timedelta object.
 * The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
 * eg. "1d 2h 3m 4s 500ms"
 * Each unit should be specified by an integer followed by its corresponding unit letter.
 *
 * @param {string} timeString - A string representing the time duration.
 * @returns {number} - The total time in milliseconds.
 */
function genTimeoutTimedelta(timeString) {
    const timeUnits = {
        'd': 24 * 60 * 60 * 1000, // days to milliseconds
        'h': 60 * 60 * 1000,      // hours to milliseconds
        'm': 60 * 1000,           // minutes to milliseconds
        's': 1000,                // seconds to milliseconds
        'ms': 1                   // milliseconds to milliseconds
    };

    const regex = /(\d+)(d|h|m|s|ms)/g;
    let match;
    let totalMilliseconds = 0;

    while ((match = regex.exec(timeString)) !== null) {
        const value = parseInt(match[1], 10);
        const unit = match[2];
        totalMilliseconds += value * timeUnits[unit];
    }

    return totalMilliseconds;
}
describe('genTimeoutTimedelta', () => {
  it('should convert "1d 2h 3m 4s 500ms" to correct timedelta', () => {
    const result = genTimeoutTimedelta("1d 2h 3m 4s 500ms");
    expect(result).toEqual({
      days: 1,
      hours: 2,
      minutes: 3,
      seconds: 4,
      milliseconds: 500
    });
  });

  it('should handle negative values correctly', () => {
    const result = genTimeoutTimedelta("-1d -2h -3m -4s -500ms");
    expect(result).toEqual({
      days: -1,
      hours: -2,
      minutes: -3,
      seconds: -4,
      milliseconds: -500
    });
  });

  it('should handle fractional values correctly', () => {
    const result = genTimeoutTimedelta("0.5d 1.5h 2.5m 3.5s 4.5ms");
    expect(result).toEqual({
      days: 0.5,
      hours: 1.5,
      minutes: 2.5,
      seconds: 3.5,
      milliseconds: 4.5
    });
  });

  it('should throw error for invalid input', () => {
    expect(() => genTimeoutTimedelta("invalid_input")).toThrow();
  });
});
