/**
 * Given an array of integers `nums`, find the length of the longest strictly increasing subsequence in it.
 *
 * @param {number[]} nums - An array of integers
 * @return {number} The length of the longest strictly increasing subsequence
 */
function lengthOfLIS(nums) {
    if (nums.length === 0) return 0;

    let dp = new Array(nums.length).fill(1);
    let maxLength = 1;

    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        maxLength = Math.max(maxLength, dp[i]);
    }

    return maxLength;
}
describe('TestLengthOfLIS', () => {
  it('should return 0 for an empty list', () => {
      expect(lengthOfLIS([])).toBe(0);
  });

  it('should return 1 for a list containing only one element', () => {
      expect(lengthOfLIS([7])).toBe(1);
  });

  it('should return 5 for a strictly increasing sequence', () => {
      expect(lengthOfLIS([1, 2, 3, 4, 5])).toBe(5);
  });

  it('should return 1 for a strictly decreasing sequence', () => {
      expect(lengthOfLIS([5, 4, 3, 2, 1])).toBe(1);
  });

  it('should return 4 for a complex sequence with mix of increasing and decreasing elements', () => {
      expect(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])).toBe(4);
  });

  it('should return 1 for a list with all elements being equal', () => {
      expect(lengthOfLIS([2, 2, 2, 2])).toBe(1);
  });

  it('should return 4 for a mix of negative and positive numbers', () => {
      expect(lengthOfLIS([-1, -2, -3, 0, 1, 2])).toBe(4);
  });
});
