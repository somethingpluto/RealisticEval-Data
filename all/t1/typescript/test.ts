describe('TestSmartConvert', () => {
    test('should convert integer', () => {
        expect(numericalStrConvert("123")).toBe(123);
    });

    test('should convert float', () => {
        expect(numericalStrConvert("123.45")).toBe(123.45);
    });

    test('should remain a string for non-numeric input', () => {
        expect(numericalStrConvert("abc")).toBe("abc");
    });

    test('should convert negative integer', () => {
        expect(numericalStrConvert("-456")).toBe(-456);
    });

    test('should convert negative float', () => {
        expect(numericalStrConvert("-456.78")).toBe(-456.78);
    });
});