/**
 * Calculates the average of the last 'period' integers in the given array of values.
 *
 * @param {number[]} values - The array of integers from which to calculate the average.
 * @param {number} period - The number of last elements to include in the average calculation.
 * @returns {number} The average of the last 'period' integers, or NaN if the input array
 *                  does not contain enough elements or if the period is invalid (<= 0).
 */
function calculate(values, period) {
    if (period <= 0) {
        return NaN;
    }
    if (values.length < period) {
        return NaN;
    }
    const lastElements = values.slice(-period);
    const sum = lastElements.reduce((acc, val) => acc + val, 0);
    return sum / period;
}
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
