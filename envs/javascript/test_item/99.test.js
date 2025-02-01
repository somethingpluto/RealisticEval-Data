/**
 * @description Calculates the sum of all the numbers in a numeric array and returns it as a model_answer_result. For example, if you enter [1, 2, 3, 4, 5], the return value is 15
 * @param {number[]} arr - The array of numbers to sum.
 */
function sum(arr) {
    return arr.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
}
describe('Sum Function Tests', () => {
    test('should return the sum of a normal array of positive numbers', () => {
        expect(sum([1, 2, 3, 4, 5])).toBe(15);
    });

    test('should return the sum of an array containing negative numbers', () => {
        expect(sum([-1, -2, -3, -4, -5])).toBe(-15);
    });

    test('should return 0 for an empty array', () => {
        expect(sum([])).toBe(0);
    });

    test('should return the sum of an array containing both positive and negative numbers', () => {
        expect(sum([10, -10, 5, -5, 15])).toBe(15);
    });

    test('should return the sum of an array with floating point numbers', () => {
        expect(sum([1.5, 2.5, 3.5])).toBe(7.5);
    });
});
