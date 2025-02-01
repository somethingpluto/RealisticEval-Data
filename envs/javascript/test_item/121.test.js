/**
 * Adjust the length of the input array according to the given target length (number). If the current length of the array is longer than the target length, the first part of the array is intercepted to match the target length; If the current length of the array is shorter than the target length, the elements in the array are repeated until the target length is reached.
 * 
 * @param {number} targetLength - The desired length for the array.
 * @param {Array} array - The input array to be adjusted.
 * @returns {Array} - A new array that has been adjusted to the target length.
 */
function adjustArrayLength(targetLength, array) {
    if (targetLength < 0) {
        throw new Error('Target length must be a non-negative number');
    }

    if (array.length === targetLength) {
        return array;
    }

    if (array.length > targetLength) {
        return array.slice(0, targetLength);
    }

    let result = [];
    for (let i = 0; i < targetLength; i++) {
        result.push(array[i % array.length]);
    }
    return result;
}
describe('adjustArrayLength function tests', () => {
    test('Array length equal to the target length', () => {
        const result = adjustArrayLength(5, [1, 2, 3, 4, 5]);
        expect(result).toEqual([1, 2, 3, 4, 5]);
    });

    test('Array length shorter than the target length', () => {
        const result = adjustArrayLength(8, [1, 2, 3]);
        expect(result).toEqual([1, 2, 3, 1, 2, 3, 1, 2]);
    });

    test('Array length shorter than the target length, target length is a multiple of array length', () => {
        const result = adjustArrayLength(6, [10, 20]);
        expect(result).toEqual([10, 20, 10, 20, 10, 20]);
    });

    test('Array length shorter than the target length, target length is not a multiple of array length', () => {
        const result = adjustArrayLength(7, [7, 14, 21]);
        expect(result).toEqual([7, 14, 21, 7, 14, 21, 7]);
    });
});
