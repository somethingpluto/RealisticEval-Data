/**
 * Reverse the order of elements in the array within the specified range [a, b].
 *
 * @param {number[]} arr - The array of integers to be modified.
 * @param {number} a - The starting index of the range to be reversed.
 * @param {number} b - The ending index of the range to be reversed.
 */
function reverseRange(arr, a, b) {
    // Ensure the range is valid
    if (a < 0 || b >= arr.length || a > b) {
        throw new Error("Invalid range specified.");
    }

    // Reverse the elements in the specified range
    while (a < b) {
        // Swap elements at indices a and b
        [arr[a], arr[b]] = [arr[b], arr[a]];
        // Move towards the center
        a++;
        b--;
    }
}
describe('reverseRange function', () => {
    test('Reverse entire array', () => {
        const v = [1, 2, 3, 4, 5];
        reverseRange(v, 0, 4);
        const expected = [5, 4, 3, 2, 1];
        expect(v).toEqual(expected);
    });

    test('Reverse subrange in the middle', () => {
        const v = [1, 2, 3, 4, 5, 6, 7, 8];
        reverseRange(v, 2, 5);
        const expected = [1, 2, 6, 5, 4, 3, 7, 8];
        expect(v).toEqual(expected);
    });

    test('Reverse a single element range', () => {
        const v = [1, 2, 3, 4, 5];
        reverseRange(v, 2, 2);
        const expected = [1, 2, 3, 4, 5];
        expect(v).toEqual(expected);
    });

    test('Reverse range with invalid indices', () => {
        const v = [1, 2, 3, 4, 5];
        reverseRange(v, -1, 3);  // Invalid start index
        const expected = [1, 2, 3, 4, 5]; // No change
        expect(v).toEqual(expected);
    });

    test('Reverse range at the end of the array', () => {
        const v = [1, 2, 3, 4, 5, 6];
        reverseRange(v, 3, 5);
        const expected = [1, 2, 3, 6, 5, 4];
        expect(v).toEqual(expected);
    });
});
