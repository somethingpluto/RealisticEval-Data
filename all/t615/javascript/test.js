describe('Test Answer', () => {
    
    test('calculate with valid input', () => {
        const values = [1, 2, 3, 4, 5];
        const period = 3;
        const expected = 4.0;  // (3 + 4 + 5) / 3
        expect(calculate(values, period)).toBe(expected);
    });

    test('calculate with all same values', () => {
        const values = [5, 5, 5, 5, 5];
        const period = 5;
        const expected = 5.0;  // (5 + 5 + 5 + 5 + 5) / 5
        expect(calculate(values, period)).toBe(expected);
    });

    test('calculate with single value', () => {
        const values = [10];
        const period = 1;
        const expected = 10.0;  // (10) / 1
        expect(calculate(values, period)).toBe(expected);
    });

    test('calculate with insufficient values', () => {
        const values = [1, 2];
        const period = 3;
        expect(isNaN(calculate(values, period))).toBe(true);  // Expecting NaN
    });

    test('calculate with empty list', () => {
        const values = [];
        const period = 1;
        expect(isNaN(calculate(values, period))).toBe(true);  // Expecting NaN
    });

    test('calculate with negative period', () => {
        const values = [1, 2, 3, 4, 5];
        const period = -1;
        expect(isNaN(calculate(values, period))).toBe(true);  // Expecting NaN
    });

});