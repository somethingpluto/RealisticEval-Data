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
    if (left >= right) {
        return;
    }

    const mid = Math.floor((left + right) / 2);

    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);

    merge(arr, left, mid, right);
}

/**
 * Merges two sorted portions of an array into a single sorted portion.
 *
 * @param {number[]} arr - The array containing the portions to be merged.
 * @param {number} left - The starting index of the first portion.
 * @param {number} mid - The ending index of the first portion and the starting
 *                      index of the second portion.
 * @param {number} right - The ending index of the second portion.
 */
function merge(arr, left, mid, right) {
    const leftArr = arr.slice(left, mid + 1);
    const rightArr = arr.slice(mid + 1, right + 1);

    let i = 0, j = 0, k = left;

    while (i < leftArr.length && j < rightArr.length) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k++] = leftArr[i++];
        } else {
            arr[k++] = rightArr[j++];
        }
    }

    while (i < leftArr.length) {
        arr[k++] = leftArr[i++];
    }

    while (j < rightArr.length) {
        arr[k++] = rightArr[j++];
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
