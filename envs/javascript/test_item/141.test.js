/**
 * Compares two arrays to determine if they contain the same unique elements, irrespective of order.
 *
 * @param {Array} arr1 - The first array to compare. Elements can be of any type.
 * @param {Array} arr2 - The second array to compare. Elements should be of the same type as the first array.
 * @returns {boolean} - Returns true if both arrays contain the same unique elements, otherwise returns false.
 */
function compareArrays(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
    }

    const sortedArr1 = arr1.slice().sort();
    const sortedArr2 = arr2.slice().sort();

    for (let i = 0; i < sortedArr1.length; i++) {
        if (sortedArr1[i] !== sortedArr2[i]) {
            return false;
        }
    }

    return true;
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
