/**
 * Calculates the minimum number of elements to delete so that the elements in the array are not duplicate.
 * 
 * Example:
 *   input: [3, 3, 1, 2, 2, 1]
 *   output: 3
 *
 * @param {Array<number>} nums - Integer array of numbers
 * @returns {number} The minimum number of moves to make every value in nums unique
 */
function minRemovalsToMakeUnique(nums) {
    const numCounts = {};
    for (const num of nums) {
        if (numCounts[num]) {
            numCounts[num]++;
        } else {
            numCounts[num] = 1;
        }
    }

    let totalRemovals = 0;
    const counts = Object.values(numCounts).sort((a, b) => b - a);
    for (const count of counts) {
        if (count > 1) {
            totalRemovals += count - 1;
        }
    }

    return totalRemovals;
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
