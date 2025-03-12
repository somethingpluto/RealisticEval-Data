// At the start of your package file
export function calculateTotalSeconds(time: [number, number?, number?, number?]): number {
  // ... existing function code ...
}

// At the end of your package file
export function parseTimeString(timeString: string): [number, number?, number?, number?] {
  const matches = timeString.match(/^(\d+)d?(\d+)?h?(\d+)?m?(\d+)?s?$/);
  if (!matches) {
    throw new Error('Invalid time string format');
  }
  return matches.slice(1).map(Number) as [number, number?, number?, number?];
}
describe('TestCalculateTotalSeconds', () => {
    it('should calculate total seconds with full values provided', () => {
        // Test with full values provided for days, hours, minutes, and seconds
        const time = [1, 2, 3, 4];  // 1 day, 2 hours, 3 minutes, 4 seconds
        const expected = 93784;
        const result = calculateTotalSeconds(time);
        expect(result).toBe(expected);
    });

    it('should calculate total seconds with some values missing', () => {
        // Test with some values missing (assumed trailing zeros)
        const time = [0, 2, 3];  // 0 days, 2 hours, 3 minutes
        const expected = 7380;
        const result = calculateTotalSeconds(time);
        expect(result).toBe(expected);
    });

    it('should calculate total seconds with only seconds provided', () => {
        // Test with only seconds provided
        const time = [0, 0, 0, 7200];  // 7200 seconds
        const expected = 7200;
        const result = calculateTotalSeconds(time);
        expect(result).toBe(expected);
    });

    it('should calculate total seconds with no time values provided', () => {
        // Test with no time values provided
        const time: [number, number?, number?, number?] = [];
        const expected = 0;
        const result = calculateTotalSeconds(time);
        expect(result).toBe(expected);
    });
});
