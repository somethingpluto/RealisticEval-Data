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