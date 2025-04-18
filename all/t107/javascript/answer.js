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

// Example usage with a large array
const largeArray = Array.from({ length: 10001 }, () => Math.floor(Math.random() * 10000));
const median = findMedian(largeArray);
console.log("Median:", median);
