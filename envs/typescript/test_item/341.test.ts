// ... (previous code for context)
function convertTimeHmsStringToMs(str: string): number {
    const regex = /^(\d+)h(\d+)m(\d+)s$/;
    const matches = str.match(regex);
    if (!matches) {
        throw new Error('Invalid time format. Expected format is "XhYmZs".');
    }
    const [_, hours, minutes, seconds] = matches;
    return parseInt(hours, 10) * 3600000 + parseInt(minutes, 10) * 60000 + parseInt(seconds, 10) * 1000;
}
// ... (continuation of the code)
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
