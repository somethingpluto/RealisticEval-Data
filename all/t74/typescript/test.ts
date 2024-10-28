describe('convertDecimalToBinary', () => {
    test('basic 32-bit conversion for 3.14', () => {
        expect(convertDecimalToBinary(3.14, 32)).toBe('01000000010010001111010111000011');
    });

    test('basic 64-bit conversion for 3.14', () => {
        expect(convertDecimalToBinary(3.14, 64)).toBe('0100000000001001000111101011100001010001111010111000010100011111');
    });

    test('advanced 32-bit conversion for 1.5', () => {
        expect(convertDecimalToBinary(1.5, 32)).toBe('00111111110000000000000000000000');
    });

    test('advanced 64-bit conversion for 1.5', () => {
        expect(convertDecimalToBinary(1.5, 64)).toBe('0011111111111000000000000000000000000000000000000000000000000000');
    });
});
