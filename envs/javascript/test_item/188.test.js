/**
 * Implement a function that performs Shell sort on an array
 * @param {number[]} arr - The array to be sorted
 */
function shellSort(arr) {
    const n = arr.length;
    let gap = Math.floor(n / 2);

    while (gap > 0) {
        for (let i = gap; i < n; i++) {
            const temp = arr[i];
            let j = i;

            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
            }

            arr[j] = temp;
        }

        gap = Math.floor(gap / 2);
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
