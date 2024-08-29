/* 
  Created by chatGPT
*/
function findMedian(arr) {
  arr.sort((a, b) => a - b); // Sort the array numerically
  const n = arr.length;
  const midIndex = Math.floor(n / 2);

  if (n % 2 === 0) {
      // Check if the array has an even number of elements
      return (arr[midIndex - 1] + arr[midIndex]) / 2;
  } else {
      // The array has an odd number of elements
      return arr[midIndex];
  }
}

// Example usage with a large array
const largeArray = Array.from({ length: 10001 }, () => Math.floor(Math.random() * 10000));
const medianLargeArray = findMedian(largeArray);
console.log("Median of largeArray:", medianLargeArray);

// Test Case 1: Odd number of elements
const arr1 = [3, 1, 4, 1, 5, 9, 2];
const median1 = findMedian(arr1);
console.log("Median of arr1:", median1); 
// Expected output: 3
// Explanation: Sorted array is [1, 1, 2, 3, 4, 5, 9]. The median is 3 (the middle element).

// Test Case 2: Even number of elements
const arr2 = [10, 2, 3, 5, 7, 8];
const median2 = findMedian(arr2);
console.log("Median of arr2:", median2); 
// Expected output: 6
// Explanation: Sorted array is [2, 3, 5, 7, 8, 10]. The median is (5 + 7) / 2 = 6.

// Test Case 3: Array with duplicate elements
const arr3 = [1, 2, 2, 2, 3];
const median3 = findMedian(arr3);
console.log("Median of arr3:", median3); 
// Expected output: 2
// Explanation: Sorted array is [1, 2, 2, 2, 3]. The median is 2 (the middle element).

// Test Case 4: Array with negative numbers
const arr4 = [-5, -10, 0, 5, 10];
const median4 = findMedian(arr4);
console.log("Median of arr4:", median4); 
// Expected output: 0
// Explanation: Sorted array is [-10, -5, 0, 5, 10]. The median is 0 (the middle element).

// Test Case 5: Array with a single element
const arr5 = [42];
const median5 = findMedian(arr5);
console.log("Median of arr5:", median5); 
// Expected output: 42
// Explanation: The array has only one element, so the median is 42.
