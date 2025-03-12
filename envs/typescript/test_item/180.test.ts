/**
 * Performs a binary search to find the index of the target value in a sorted array.
 * If the target value is not found, it returns the index of the closest value.
 *
 * @param {number[]} array - The sorted array in which to search.
 * @param {number} target - The target value to search for.
 * @returns {number} The index of the target or the index of the closest value if the target is not found.
 */
function binarySearchClosest(array: number[], target: number): number {
    let left = 0;
    let right = array.length - 1;
    let closestIndex = 0;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (array[mid] === target) {
            return mid;
        }

        if (Math.abs(array[mid] - target) < Math.abs(array[closestIndex] - target)) {
            closestIndex = mid;
        }

        if (array[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return closestIndex;
}
describe('binarySearchClosest', () => {
    
    test('target present', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 7;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(3); // Target should be found at index 3.
    });

    test('closest element smaller', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 6;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(2); // Closest element should be 5 at index 2.
    });

    test('closest element larger', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 8;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(3); // Closest element should be 7 at index 3.
    });

    test('target smaller than all', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 0;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(0); // Closest element should be 1 at index 0.
    });

    test('target larger than all', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 12;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(5); // Closest element should be 11 at index 5.
    });
});
