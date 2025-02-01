/**
 * Implement a function that performs Shell sort on an array
 * @param {number[]} arr - The array to be sorted
 */
function shellSort(arr) {
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

// Example usage:
// let arr = [12, 34, 54, 2, 3];
// shellSort(arr);
// console.log(arr); // Output will be the sorted array
function isSorted(arr) {
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
}

// Test suite for shellSort
describe('Shell sort', () => {
    test('Basic functionality', () => {
        // Test Case 1: Already sorted array
        let arr1 = [1, 2, 3, 4, 5];
        shellSort(arr1);
        expect(isSorted(arr1)).toBe(true);

        // Test Case 2: Reverse sorted array
        let arr2 = [5, 4, 3, 2, 1];
        shellSort(arr2);
        expect(isSorted(arr2)).toBe(true);

        // Test Case 3: Array with duplicate elements
        let arr3 = [4, 2, 2, 4, 1];
        shellSort(arr3);
        expect(isSorted(arr3)).toBe(true);

        // Test Case 4: Array with negative numbers
        let arr4 = [-3, -1, -4, -2, 0];
        shellSort(arr4);
        expect(isSorted(arr4)).toBe(true);

        // Test Case 5: Empty array
        let arr5 = [];
        shellSort(arr5);
        expect(isSorted(arr5)).toBe(true);
    });
});
