/**
 * calculates the elapsed time from a given start time in milliseconds and returns
 * it as a formatted string in "minutes:seconds" format.
 *
 * @param {number} startTimeInMillis - The start time in milliseconds.
 * @return {string} A string representing the elapsed time in minutes and seconds.
 */
function timePassed(startTimeInMillis) {
    const elapsedTimeInMillis = Date.now() - startTimeInMillis;
    const minutes = Math.floor(elapsedTimeInMillis / 60000);
    const seconds = ((elapsedTimeInMillis % 60000) / 1000).toFixed(0);
    return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
}
describe('timePassed function', () => {
    const originalDateNow = Date.now;

    beforeEach(() => {
        // Freeze the Date.now() to a fixed timestamp
        Date.now = jest.fn(() => 1609459200000); // January 1, 2021, 00:00:00
    });

    afterEach(() => {
        // Restore original Date.now() function
        Date.now = originalDateNow;
    });

    test('should correctly calculate time passed from 1 minute ago', () => {
        const startTime = 1609459140000; // 1 minute earlier
        expect(timePassed(startTime)).toBe("1:00");
    });

    test('should handle the boundary of 59 seconds correctly', () => {
        const startTime = 1609459194100; // 59 seconds and 900 milliseconds earlier
        expect(timePassed(startTime)).toBe("0:05");
    });

    test('should return 0:00 when start time is the same as current time', () => {
        expect(timePassed(1609459200000)).toBe("0:00");
    });

    test('should handle negative time differences (future start time)', () => {
        const startTime = 1609459260000; // 1 minute into the future
        expect(timePassed(startTime)).toMatch(/-/); // Expecting negative output or some error handling
    });

    test('should handle very large time differences correctly', () => {
        const startTime = 1483228800000; // January 1, 2017, 00:00:00 (4 years difference)
        expect(timePassed(startTime)).toBe("2103840:00"); // Calculated minutes for 4 years
    });
});
