import { isEqual } from 'lodash';

/**
 * Compares two arrays to determine if they contain the same unique elements, irrespective of order.
 * Now includes type checking and uses lodash's isEqual for deep comparison.
 *
 * @param {Array<T>} arr1 - The first array to compare. Elements can be of any type T.
 * @param {Array<T>} arr2 - The second array to compare. Elements should be of the same type as the first array.
 * @returns {boolean} - Returns true if both arrays contain the same unique elements, otherwise returns false.
 *
 * @template T - The type of the elements in the arrays.
 */
function compareArrays<T>(arr1: Array<T>, arr2: Array<T>): boolean {
  if (!Array.isArray(arr1) || !Array.isArray(arr2)) {
    throw new Error('Both inputs must be arrays.');
  }
  return isEqual(arr1.sort(), arr2.sort());
}
describe('compareArrays', () => {
    test('should return true for identical arrays with same order', () => {
        const arr1 = [1, 2, 3];
        const arr2 = [1, 2, 3];
        expect(compareArrays(arr1, arr2)).toBe(true);
    });

    test('should return true for identical arrays with different order', () => {
        const arr1 = [3, 2, 1];
        const arr2 = [1, 2, 3];
        expect(compareArrays(arr1, arr2)).toBe(true);
    });

    test('should return false for arrays with different elements', () => {
        const arr1 = [1, 2, 3];
        const arr2 = [4, 5, 6];
        expect(compareArrays(arr1, arr2)).toBe(false);
    });

    test('should return false for arrays with different lengths', () => {
        const arr1 = [1, 2, 3];
        const arr2 = [1, 2];
        expect(compareArrays(arr1, arr2)).toBe(false);
    });

    test('should return true for arrays with duplicate elements but same unique set', () => {
        const arr1 = [1, 1, 2, 3, 3];
        const arr2 = [3, 2, 1, 1];
        expect(compareArrays(arr1, arr2)).toBe(true);
    });
});
