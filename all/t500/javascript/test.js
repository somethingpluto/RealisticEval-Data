describe('TestConvertScoreToDecimal', () => {
    test('test_decimal_score', () => {
        // Test a simple decimal score
        expect(convertScoreToDecimal("2.5")).toBe(2.5);
    });

    test('test_fraction_score', () => {
        // Test a fraction score
        expect(convertScoreToDecimal("10/4")).toBe(2.5);
    });

    test('test_integer_score', () => {
        // Test an integer score represented as a string
        expect(convertScoreToDecimal("5")).toBe(5.0);
    });

    test('test_integer_divide_score', () => {
        // Test an integer divide score
        expect(convertScoreToDecimal("12/3")).toBe(4.0);
    });
});