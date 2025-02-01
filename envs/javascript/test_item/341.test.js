/**
 * Converts a time string in the format "XhYmZs" (hours, minutes, seconds) into milliseconds.
 *
 * @param {string} str - The input string representing the time duration.
 * @returns {number} The time in milliseconds.
 * @throws {Error} If the input string does not match the expected format.
 */
function convertTimeHmsStringToMs(str) {
    const regex = /^(\d+)h(\d+)m(\d+)s$/;
    const match = str.match(regex);

    if (!match) {
        throw new Error('Input string does not match the expected format "XhYmZs".');
    }

    const hours = parseInt(match[1], 10);
    const minutes = parseInt(match[2], 10);
    const seconds = parseInt(match[3], 10);

    const totalMs = hours * 3600000 + minutes * 60000 + seconds * 1000;

    return totalMs;
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
