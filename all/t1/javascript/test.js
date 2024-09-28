describe('numericalStrConvert', () => {
    test('should convert to integer', () => {
        expect(numericalStrConvert("123")).toBe(123);
    });

    test('should convert to float', () => {
        expect(numericalStrConvert("123.45")).toBe(123.45);
    });

    test('should remain a string for non-numeric input', () => {
        expect(numericalStrConvert("abc")).toBe("abc");
    });

    test('should convert to negative integer', () => {
        expect(numericalStrConvert("-456")).toBe(-456);
    });

    test('should convert to negative float', () => {
        expect(numericalStrConvert("-456.78")).toBe(-456.78);
    });
});