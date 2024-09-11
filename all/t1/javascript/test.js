describe('convertString', () => {
    test('converts a valid integer string', () => {
        expect(convertString("123")).toBe(123);
    });

    test('converts a valid float string', () => {
        expect(convertString("123.45")).toBe(123.45);
    });

    test('returns the original string when it contains letters', () => {
        expect(convertString("123abc")).toBe("123abc");
    });

    test('returns the original string when it is non-numeric', () => {
        expect(convertString("hello")).toBe("hello");
    });

    test('handles strings with spaces around numbers correctly', () => {
        expect(convertString("   678   ")).toBe(678);
    });
});