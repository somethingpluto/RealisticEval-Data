/**
 * Finds the median of a given array of numbers.
 * 
 * @param {number[]} arr - The array of numbers to find the median of.
 * @returns {number} - The median of the array.
 */
function findMedian(arr) {
    // Sort the array in ascending order
    arr.sort((a, b) => a - b);
    
    const n = arr.length;
    const midIndex = Math.floor(n / 2);

    // Determine if the array length is even or odd and return the median
    if (n % 2 === 0) {
        // Even number of elements: average the two middle elements
        return (arr[midIndex - 1] + arr[midIndex]) / 2;
    } else {
        // Odd number of elements: return the middle element
        return arr[midIndex];
    }
}

// Test Case 1: Odd number of elements
const arr1 = [3, 1, 4, 1, 5, 9, 2];
const median1 = findMedian(arr1);
console.log(median1); 
// Expected output: 3
// Explanation: Sorted array is [1, 1, 2, 3, 4, 5, 9]. The median is 3 (the middle element).

// Test Case 2: Even number of elements
const arr2 = [10, 2, 3, 5, 7, 8];
const median2 = findMedian(arr2);
console.log(median2); 
// Expected output: 6
// Explanation: Sorted array is [2, 3, 5, 7, 8, 10]. The median is (5 + 7) / 2 = 6.

// Test Case 3: Array with duplicate elements
const arr3 = [1, 2, 2, 2, 3];
const median3 = findMedian(arr3);
console.log(median3); 
// Expected output: 2
// Explanation: Sorted array is [1, 2, 2, 2, 3]. The median is 2 (the middle element).

// Test Case 4: Array with negative numbers
const arr4 = [-5, -10, 0, 5, 10];
const median4 = findMedian(arr4);
console.log(median4); 
// Expected output: 0
// Explanation: Sorted array is [-10, -5, 0, 5, 10]. The median is 0 (the middle element).

// Test Case 5: Array with a single element
const arr5 = [42];
const median5 = findMedian(arr5);
console.log(median5); 
// Expected output: 42
// Explanation: The array has only one element, so the median is 42.
