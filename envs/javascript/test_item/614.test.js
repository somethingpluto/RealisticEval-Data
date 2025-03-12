/**
 * Calculates the average difference between consecutive integers in the provided array.
 *
 * @param {number[]} numbers - An array of integers.
 * @returns {number} The average difference between consecutive integers, or 0 if there are fewer than 2 integers.
 */
function calculateAverageDifference(numbers) {
    if (numbers.length < 2) {
        return 0;
    }

    let totalDifference = 0;
    for (let i = 1; i < numbers.length; i++) {
        totalDifference += Math.abs(numbers[i] - numbers[i - 1]);
    }

    return totalDifference / (numbers.length - 1);
}
describe('calculateAverageDifference', () => {
    test('calculates average difference for positive integers', () => {
        const numbers = [10, 20, 30, 40];
        const result = calculateAverageDifference(numbers);
        const expected = 10.0;
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });

    test('calculates average difference for mixed positive and negative integers', () => {
        const numbers = [-10, 0, 10, 20];
        const result = calculateAverageDifference(numbers);
        const expected = 10.0;
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });

    test('calculates average difference for same values', () => {
        const numbers = [5, 5, 5, 5];
        const result = calculateAverageDifference(numbers);
        const expected = 0.0;
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });

    test('returns 0 for single element list', () => {
        const numbers = [100];
        const result = calculateAverageDifference(numbers);
        const expected = 0.0; // Not enough data to calculate differences
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });

    test('returns 0 for empty list', () => {
        const numbers = [];
        const result = calculateAverageDifference(numbers);
        const expected = 0.0; // Not enough data to calculate differences
        expect(result).toBeCloseTo(expected, 5); // Jest equivalent for almost equal assertion
    });
});
