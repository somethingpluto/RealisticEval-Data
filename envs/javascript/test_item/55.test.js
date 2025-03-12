/**
 * Calculates the minimum number of elements to delete so that the elements in the array are not duplicate.
 * 
 * @param {Array<number>} nums - Integer array of numbers
 * @returns {number} The minimum number of moves to make every value in nums unique
 */
function minRemovalsToMakeUnique(nums) {
    // Create a frequency map to count occurrences of each number
    const frequencyMap = new Map();
    
    for (const num of nums) {
        if (frequencyMap.has(num)) {
            frequencyMap.set(num, frequencyMap.get(num) + 1);
        } else {
            frequencyMap.set(num, 1);
        }
    }
    
    // Create an array to store the counts of each number
    const counts = Array.from(frequencyMap.values());
    
    // Sort the counts in descending order
    counts.sort((a, b) => b - a);
    
    let removals = 0;
    const uniqueCounts = new Set();
    
    for (const count of counts) {
        let currentCount = count;
        
        // Ensure the current count is unique
        while (currentCount > 0 && uniqueCounts.has(currentCount)) {
            currentCount--;
            removals++;
        }
        
        if (currentCount > 0) {
            uniqueCounts.add(currentCount);
        }
    }
    
    return removals;
}
describe('TestMinRemovalsToMakeUnique', () => {
  test('test_basic_array', () => {
      /** Test with a basic array where multiple removals are needed. */
      expect(minRemovalsToMakeUnique([3, 3, 1, 2, 2, 1])).toBe(3);
  });

  test('test_all_identical', () => {
      /** Test an array where all elements are identical. */
      expect(minRemovalsToMakeUnique([4, 4, 4, 4])).toBe(3);
  });

  test('test_all_unique', () => {
      /** Test an array where all elements are already unique. */
      expect(minRemovalsToMakeUnique([1, 2, 3, 4])).toBe(0);
  });

  test('test_empty_array', () => {
      /** Test an empty array. */
      expect(minRemovalsToMakeUnique([])).toBe(0);
  });

  test('test_complex_case', () => {
      /** Test a more complex case with a larger array. */
      expect(minRemovalsToMakeUnique([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])).toBe(6);
  });
});
