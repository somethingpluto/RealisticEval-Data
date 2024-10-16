/**
 * Implements the Bubble Sort algorithm.
 *
 * This function sorts an array of integers in ascending order using the Bubble Sort algorithm.
 * The algorithm works by repeatedly stepping through the list, comparing adjacent elements, and
 * swapping them if they are in the wrong order. The process is repeated until the list is sorted.
 *
 * @param {number[]} arr - An array of integers to be sorted.
 */
function bubbleSort(arr) {
    let swapped;
    let n = arr.length;
    do {
        swapped = false;
        for (let i = 1; i < n; i++) {
            if (arr[i - 1] > arr[i]) {
                // Swap the elements
                [arr[i - 1], arr[i]] = [arr[i], arr[i - 1]];
                swapped = true;
            }
        }
        n--; // Reduce the range of comparison, as the last element is now sorted
    } while (swapped);
}