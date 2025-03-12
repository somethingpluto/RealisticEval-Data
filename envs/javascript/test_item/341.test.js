/**
 * Converts a time string in the format "XhYmZs" (hours, minutes, seconds) into milliseconds.
 *
 * @param str The input string representing the time duration.
 * @returns The time in milliseconds.
 * @throws Error if the input string does not match the expected format.
 */
function convertTimeHmsStringToMs(str) {
    const timePattern = /^(\d+h)?(\d+m)?(\d+s)?$/;
    if (!timePattern.test(str)) {
        throw new Error("Invalid time format. Expected format is 'XhYmZs'.");
    }

    const hoursMatch = str.match(/(\d+)h/);
    const minutesMatch = str.match(/(\d+)m/);
    const secondsMatch = str.match(/(\d+)s/);

    const hours = hoursMatch ? parseInt(hoursMatch[1], 10) : 0;
    const minutes = minutesMatch ? parseInt(minutesMatch[1], 10) : 0;
    const seconds = secondsMatch ? parseInt(secondsMatch[1], 10) : 0;

    const totalMilliseconds = (hours * 3600 + minutes * 60 + seconds) * 1000;
    return totalMilliseconds;
}
describe('convertTimeHmsStringToMs', () => {
    test('converts typical time string correctly (1h30m15s)', () => {
        const result = convertTimeHmsStringToMs('1h30m15s');
        expect(result).toBe(5415000);  // 1 hour + 30 minutes + 15 seconds in ms
    });

    test('correctly converts string with zero values (0h0m0s)', () => {
        const result = convertTimeHmsStringToMs('0h0m0s');
        expect(result).toBe(0);  // 0 ms
    });

    test('converts maximum single digit values (9h59m59s)', () => {
        const result = convertTimeHmsStringToMs('9h59m59s');
        expect(result).toBe(35999000); // 9 hours + 59 minutes + 59 seconds in ms
    });

    test('handles large values (100h0m0s)', () => {
        const result = convertTimeHmsStringToMs('100h0m0s');
        expect(result).toBe(360000000); // 100 hours in ms
    });

    test('correctly converts strings with leading zeros (01h01m01s)', () => {
        const result = convertTimeHmsStringToMs('01h01m01s');
        expect(result).toBe(3661000); // 1 hour + 1 minute + 1 second in ms
    });
});
