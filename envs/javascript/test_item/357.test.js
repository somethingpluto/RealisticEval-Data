/**
 * Sorts an array of integers using the Hill Sort (Shell Sort) algorithm.
 *
 * @param {number[]} arr An array of integers that will be sorted in-place.
 */
function hillSort(arr) {
    let n = arr.length;
    // Start with a big gap, then reduce the gap
    for (let gap = Math.floor(n / 2); gap > 0; gap = Math.floor(gap / 2)) {
        // Do a gapped insertion sort for this gap size.
        // The first gap elements a[0..gap-1] are already in gapped order
        // keep adding one more element until the entire array is gap sorted
        for (let i = gap; i < n; i += 1) {
            // add a[i] to the elements that have been gap sorted
            // save a[i] in temp and make a hole at position i
            let temp = arr[i];
            // shift earlier gap-sorted elements up until the correct location for a[i] is found
            let j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            // put temp (the original a[i]) in its correct location
            arr[j] = temp;
        }
    }
}
function isSorted(arr) {
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
}

// Test cases
describe('Hill Sort', () => {
    test('Sort an already sorted array', () => {
        const arr = [1, 2, 3, 4, 5];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test('Sort an array in reverse order', () => {
        const arr = [5, 4, 3, 2, 1];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test('Sort an array with duplicate values', () => {
        const arr = [3, 1, 2, 3, 2];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test('Sort an array with all identical values', () => {
        const arr = [1, 1, 1, 1, 1];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test('Sort an empty array', () => {
        const arr = [];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test('Sort an array with one element', () => {
        const arr = [42];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });

    test('Sort a large random array', () => {
        const arr = [3, 7, 2, 5, 1, 4, 6, 0, 9, 8];
        hillSort(arr);
        expect(isSorted(arr)).toBe(true);
    });
});
