describe('Hexadecimal String to Float Conversion', () => {
    test('Positive number: 40490FDB', () => {
        const hexStr = '40490FDB'; // 3.14159 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(3.14159, 5); // 5 decimal places precision
    });

    test('Negative number: C0490FDB', () => {
        const hexStr = 'C0490FDB'; // -3.14159 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(-3.14159, 5); // 5 decimal places precision
    });

    test('Zero: 00000000', () => {
        const hexStr = '00000000'; // 0.0 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(0.0, 5); // 5 decimal places precision
    });

    test('Small positive number: 3F800000', () => {
        const hexStr = '3F800000'; // 1.0 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(1.0, 5); // 5 decimal places precision
    });

    test('Small negative number: BF800000', () => {
        const hexStr = 'BF800000'; // -1.0 in float
        const result = hexStringToFloat(hexStr);
        expect(result).toBeCloseTo(-1.0, 5); // 5 decimal places precision
    });
});