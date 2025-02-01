/**
 * Sorts a portion of an array using the merge sort algorithm.
 *
 * @param {number[]} arr - An array of integers that contains the
 *                         elements to be sorted.
 * @param {number} left - The starting index of the portion of the array to be
 *                       sorted.
 * @param {number} right - The ending index of the portion of the array to be
 *                        sorted.
 */
function mergeSort(arr, left, right) {
    if (left < right) {
        // Find the middle point to divide the array into two halves
        let middle = Math.floor((left + right) / 2);

        // Call mergeSort for the first half
        mergeSort(arr, left, middle);

        // Call mergeSort for the second half
        mergeSort(arr, middle + 1, right);

        // Merge the two halves sorted in step 2 and 3
        merge(arr, left, middle, right);
    }
}

/**
 * Merges two halves of an array.
 *
 * @param {number[]} arr - The array to be sorted.
 * @param {number} left - The starting index of the first half.
 * @param {number} middle - The ending index of the first half and starting index of the second half.
 * @param {number} right - The ending index of the second half.
 */
function merge(arr, left, middle, right) {
    // Find the sizes of the two halves
    let n1 = middle - left + 1;
    let n2 = right - middle;

    /* Create temp arrays */
    let L = new Array(n1);
    let R = new Array(n2);

    /* Copy data to temp arrays */
    for (let i = 0; i < n1; ++i) {
        L[i] = arr[left + i];
    }
    for (let j = 0; j < n2; ++j) {
        R[j] = arr[middle + 1 + j];
    }

    /* Merge the temp arrays */

    // Initial indexes of first and second subarrays
    let i = 0, j = 0;

    // Initial index of merged subarray array
    let k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    /* Copy the remaining elements of L[], if there are any */
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of R[], if there are any */
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
describe("Merge Sort Test Cases", () => {
    test("Sorting an empty array", () => {
        const emptyArray = [];
        mergeSort(emptyArray, 0, emptyArray.length - 1);
        expect(emptyArray).toEqual([]);
    });

    test("Sorting a single element array", () => {
        const singleElement = [1];
        mergeSort(singleElement, 0, singleElement.length - 1);
        expect(singleElement).toEqual([1]);
    });

    test("Sorting a sorted array", () => {
        const sortedArray = [1, 2, 3, 4, 5];
        mergeSort(sortedArray, 0, sortedArray.length - 1);
        expect(sortedArray).toEqual([1, 2, 3, 4, 5]); // Fixed expected result
    });

    test("Sorting a reverse sorted array", () => {
        const reverseSortedArray = [5, 4, 3, 2, 1];
        mergeSort(reverseSortedArray, 0, reverseSortedArray.length - 1);
        expect(reverseSortedArray).toEqual([1, 2, 3, 4, 5]);
    });

    test("Sorting an array with random integers", () => {
        const randomArray = [38, 27, 43, 3, 9, 82, 10];
        const expectedSortedArray = [3, 9, 10, 27, 38, 43, 82];
        mergeSort(randomArray, 0, randomArray.length - 1);
        expect(randomArray).toEqual(expectedSortedArray);
    });
});
