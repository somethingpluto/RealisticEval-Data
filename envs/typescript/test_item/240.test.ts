import { parseDuration } from 'date-fns';

/**
 * Converts a time duration string into a `Date` object.
 * The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
 * e.g. "1d 2h 3m 4s 500ms"
 * Each unit should be specified by an integer followed by its corresponding unit letter.
 *
 * @param {string} timeString - A string representing the time duration.
 * @returns {Date} - A Date object representing the input duration.
 */
function genTimeoutDuration(timeString: string): Date {
  const duration = parseDuration(timeString);
  const now = new Date();
  return new Date(now.getTime() + duration.milliseconds);
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

  it('should convert "2h 30m" to correct timedelta', () => {
    const result = genTimeoutTimedelta("2h 30m");
    expect(result).toEqual({
      days: 0,
      hours: 2,
      minutes: 30,
      seconds: 0,
      milliseconds: 0
    });
  });

  it('should convert "1s" to correct timedelta', () => {
    const result = genTimeoutTimedelta("1s");
    expect(result).toEqual({
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 1,
      milliseconds: 0
    });
  });

  it('should convert "500ms" to correct timedelta', () => {
    const result = genTimeoutTimedelta("500ms");
    expect(result).toEqual({
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 0,
      milliseconds: 500
    });
  });

  it('should handle empty string', () => {
    const result = genTimeoutTimedelta("");
    expect(result).toEqual({
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 0,
      milliseconds: 0
    });
  });

  it('should throw error for invalid input', () => {
    expect(() => genTimeoutTimedelta("invalid_input")).toThrowError();
  });
});
