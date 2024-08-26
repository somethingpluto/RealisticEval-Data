describe('convertTimeHmsStringToMs', () => {
    test('converts typical time string correctly (1h30m15s)', () => {
        const result = convertTimeHmsStringToMs('1h30m15s');
        expect(result).toBe(5415000);  // 1 hour + 30 minutes + 15 seconds in ms
    });

    test('handles time string with missing units correctly (45m30s)', () => {
        const result = convertTimeHmsStringToMs('45m30s');
        expect(result).toBe(2730000);  // 45 minutes + 30 seconds in ms
    });

    test('correctly converts string with zero values (0h0m0s)', () => {
        const result = convertTimeHmsStringToMs('0h0m0s');
        expect(result).toBe(0);  // 0 ms
    });

    test('throws error on empty string', () => {
        expect(() => convertTimeHmsStringToMs('')).toThrow();
    });

});
/**
 * Converts a time string in the format "XhYmZs" (hours, minutes, seconds) into milliseconds.
 *
 * @param str The input string representing the time duration.
 * @returns The time in milliseconds.
 * @throws Error if the input string does not match the expected format.
 */
const convertTimeHmsStringToMs = (str: string): number => {
    if (str == "") {
        throw new Error("str is empty")
    }
    // Extended regular expression to parse both short and verbose time formats
    const regex = /(?:(\d+)(h|hours))? ?(?:(\d+)(m|mins|minutes))? ?(?:(\d+)(s|secs|seconds))?/;
    const match = str.match(regex);

    if (!match) {
        throw new Error(`Cannot convert hms string "${str}" to ms!`);
    }

    // Parse hours, minutes, and seconds, defaulting to 0 if any group is missing
    // Note: Hours are in index 1, minutes in index 3, and seconds in index 5
    const hours = parseInt(match[1] || '0', 10);
    const minutes = parseInt(match[3] || '0', 10);
    const seconds = parseInt(match[5] || '0', 10);

    // Calculate the total milliseconds
    const totalMilliseconds = ((hours * 60 + minutes) * 60 + seconds) * 1000;
    return totalMilliseconds;
};