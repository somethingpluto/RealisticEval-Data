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
  const median = findMedian(largeArray);
  console.log("Median:", median);