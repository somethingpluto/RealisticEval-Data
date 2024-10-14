describe('isValidPortNumber', () => {
    test('returns true for a valid port number in the middle of the range', () => {
        expect(isValidPortNumber(8080)).toBe(true);
    });

    test('returns true for the lowest valid port number', () => {
        expect(isValidPortNumber(1)).toBe(true);
    });

    test('returns true for the highest valid port number', () => {
        expect(isValidPortNumber(65535)).toBe(true);
    });

    test('returns false for a port number below the valid range', () => {
        expect(isValidPortNumber(0)).toBe(false);
    });

    test('returns false for a port number above the valid range', () => {
        expect(isValidPortNumber(65536)).toBe(false);
    });
});