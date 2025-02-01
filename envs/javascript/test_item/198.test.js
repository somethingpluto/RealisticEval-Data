/**
 * Finds the maximum difference between elements in the array
 * such that the smaller element appears before the larger one.
 *
 * @param {number[]} l An array of integers containing the elements.
 * @return {number} The maximum difference.
 */
function findMaxDifference(l) {
    if (l.length < 2) {
        return 0;
    }

    let minElement = l[0];
    let maxDifference = 0;

    for (let i = 1; i < l.length; i++) {
        if (l[i] < minElement) {
            minElement = l[i];
        } else {
            maxDifference = Math.max(maxDifference, l[i] - minElement);
        }
    }

    return maxDifference;
}
describe('findMaxDifference', () => {
    test('General case', () => {
        const l = [2, 3, 10, 6, 4, 8, 1];
        expect(findMaxDifference(l)).toBe(8);  // Maximum difference is 10 - 2 = 8
    });

    test('Decreasing sequence', () => {
        const l = [10, 9, 8, 7, 6, 5];
        expect(findMaxDifference(l)).toBe(0);  // Maximum difference should be 0, as all differences are negative
    });

    test('All elements the same', () => {
        const l = [5, 5, 5, 5, 5];
        expect(findMaxDifference(l)).toBe(0);  // Maximum difference is 5 - 5 = 0
    });

    test('Only two elements', () => {
        const l = [3, 8];
        expect(findMaxDifference(l)).toBe(5);  // Maximum difference is 8 - 3 = 5
    });

    test('Single element', () => {
        const l = [4];
        expect(findMaxDifference(l)).toBe(0);  // Only one element, no difference to calculate
    });
});
