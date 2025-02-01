/**
 * Implements the Bubble Sort algorithm.
 *
 * @param {number[]} arr - An array of integers to be sorted.
 */
function bubbleSort(arr) {
    let n = arr.length;
    let swapped;
    do {
        swapped = false;
        for (let i = 1; i < n; i++) {
            if (arr[i - 1] > arr[i]) {
                // Swap the elements
                let temp = arr[i - 1];
                arr[i - 1] = arr[i];
                arr[i] = temp;
                swapped = true;
            }
        }
        // Reduce n by 1 because the last element is already in place
        n--;
    } while (swapped);
}
describe("BubbleSort Test Cases", () => {
    // Test Case 1: Sorting an already sorted array
    test("should sort an already sorted array", () => {
        const arr1 = [1, 2, 3, 4, 5];
        bubbleSort(arr1);
        expect(arr1).toEqual([1, 2, 3, 4, 5]);
    });

    // Test Case 2: Sorting a reverse sorted array
    test("should sort a reverse sorted array", () => {
        const arr2 = [5, 4, 3, 2, 1];
        bubbleSort(arr2);
        expect(arr2).toEqual([1, 2, 3, 4, 5]);
    });

    // Test Case 3: Sorting an array with duplicate elements
    test("should sort an array with duplicate elements", () => {
        const arr3 = [3, 1, 2, 3, 2];
        bubbleSort(arr3);
        expect(arr3).toEqual([1, 2, 2, 3, 3]);
    });

    // Test Case 4: Sorting an array with a single element
    test("should sort an array with a single element", () => {
        const arr4 = [1];
        bubbleSort(arr4);
        expect(arr4).toEqual([1]);
    });

    // Test Case 5: Sorting an empty array
    test("should sort an empty array", () => {
        const arr5 = [];
        bubbleSort(arr5);
        expect(arr5).toEqual([]);
    });
});
