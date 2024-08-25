describe('getArrayAverage', () => {
    test('should return the average of an array of positive integers', () => {
        const result = getArrayAverage([1, 2, 3, 4, 5]);
        expect(result).toBe(3); // (1 + 2 + 3 + 4 + 5) / 5 = 3
    });

    test('should return the average of an array with negative numbers', () => {
        const result = getArrayAverage([-1, -2, -3, -4, -5]);
        expect(result).toBe(-3); // (-1 + -2 + -3 + -4 + -5) / 5 = -3
    });

    test('should return the average of an array with mixed positive and negative numbers', () => {
        const result = getArrayAverage([1, -1, 2, -2, 3, -3]);
        expect(result).toBe(0); // (1 + -1 + 2 + -2 + 3 + -3) / 6 = 0
    });

    test('should handle an empty array (edge case)', () => {
        const result = getArrayAverage([]);
        expect(result).toBeNaN(); // Division by zero, expected result is NaN
    });

    test('should return the single element when the array contains one item', () => {
        const result = getArrayAverage([7]);
        expect(result).toBe(7); // The average of [7] is 7
    });
});
function getArrayAverage(array) {
    let sum = 0;
    for (let i = 0; i < array.length; i++) {
        sum += array[i]
    }
    return sum / array.length
}