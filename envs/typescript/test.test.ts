const convertTimeHmsStringToMs = (str: string): number => {
    const regex = /^(\d+)h(\d+)m(\d+)s$/;
    const match = str.match(regex);
    if (!match) {
        throw new Error("Input string does not match the expected format.");
    }
    const hours = parseInt(match[1]);
    const minutes = parseInt(match[2]);
    const seconds = parseInt(match[3]);
    return (hours * 3600 + minutes * 60 + seconds) * 1000;
};
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
        expect(() => convertTimeHmsStringToMs('')).toThrow('Cannot convert hms string "" to ms!');
    });

    test('throws error on invalid format (not following hms pattern)', () => {
        expect(() => convertTimeHmsStringToMs('2hours15mins')).toThrow('Cannot convert hms string "2hours15mins" to ms!');
    });
});
