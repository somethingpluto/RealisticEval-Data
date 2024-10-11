describe('numericalStrConvert', () => {
    test('should convert integer string to number', () => {
        expect(numericalStrConvert("123")).toBe(123);
    });

    test('should convert float string to number', () => {
        expect(numericalStrConvert("123.45")).toBe(123.45);
    });

    test('should return non-numerical string as is', () => {
        expect(numericalStrConvert("hello")).toBe("hello");
    });

    test('should convert negative float string to number', () => {
        expect(numericalStrConvert("-123.45")).toBe(-123.45);
    });
});