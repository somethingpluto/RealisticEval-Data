/**
 * Performs a binary search to find the index of the target value in a sorted array.
 * If the target value is not found, it returns the index of the closest value.
 *
 * @param {Array<number>} array - The sorted array in which to search.
 * @param {number} target - The target value to search for.
 * @returns {number} The index of the target or the index of the closest value if the target is not found.
 */
function binarySearchClosest(array, target) {
    let left = 0;
    let right = array.length - 1;
    let closestIndex = -1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const midValue = array[mid];

        if (midValue === target) {
            return mid;
        } else if (midValue < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }

        // Update the closest index if the current mid value is closer to the target
        if (closestIndex === -1 || Math.abs(array[mid] - target) < Math.abs(array[closestIndex] - target)) {
            closestIndex = mid;
        }
    }

    return closestIndex;
}
describe('binarySearchClosest', () => {
    test('Target is present in the array', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 7;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(3); // Target should be found at index 3.
    });

    test('Closest element is smaller than target', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 6;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(2); // Closest element should be 5 at index 2.
    });

    test('Closest element is larger than target', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 8;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(3); // Closest element should be 7 at index 3.
    });

    test('Target is smaller than all elements', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 0;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(0); // Closest element should be 1 at index 0.
    });

    test('Target is larger than all elements', () => {
        const array = [1, 3, 5, 7, 9, 11];
        const target = 12;
        const result = binarySearchClosest(array, target);
        expect(result).toBe(5); // Closest element should be 11 at index 5.
    });
});
