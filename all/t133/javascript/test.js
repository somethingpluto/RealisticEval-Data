describe('isSignificantNumber', () => {
    test('should return true for a valid significant number with exactly 5 digits', () => {
        expect(isSignificantNumber("12345")).toBe(true);
    });

    test('should return false for a number with leading zero', () => {
        expect(isSignificantNumber("01234")).toBe(false);
    });

    test('should return true for a valid significant number with exactly 18 digits', () => {
        expect(isSignificantNumber("123456789012345678")).toBe(true);
    });

    test('should return false for a number with less than 5 digits', () => {
        expect(isSignificantNumber("123")).toBe(false);
    });

    test('should return false for a number with more than 18 digits', () => {
        expect(isSignificantNumber("1234567890123456789")).toBe(false);
    });

    test('should return false for a number containing non-digit characters', () => {
        expect(isSignificantNumber("1234a")).toBe(false);
    });

    test('should return false for a single zero', () => {
        expect(isSignificantNumber("0")).toBe(false);
    });

    test('should return false for non-string input', () => {
        expect(isSignificantNumber(12345)).toBe(false);
    });
});