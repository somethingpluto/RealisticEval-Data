describe('numericalStrConvert', () => {
    test('should convert string "123" to integer', () => {
        expect(numericalStrConvert("123")).toBe(123);
    });

    test('should convert string "123.45" to float', () => {
        expect(numericalStrConvert("123.45")).toBe(123.45);
    });

    test('should keep non-numeric string "abc" as a string', () => {
        expect(numericalStrConvert("abc")).toBe("abc");
    });

    test('should convert string "-456" to negative integer', () => {
        expect(numericalStrConvert("-456")).toBe(-456);
    });

    test('should convert string "-456.78" to negative float', () => {
        expect(numericalStrConvert("-456.78")).toBe(-456.78);
    });
});