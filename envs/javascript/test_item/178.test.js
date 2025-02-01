/**
 * Find the longest non-decreasing subsequence in the given array.
 *
 * @param {number[]} nums - The input array of integers.
 * @returns {number[]} A list containing the longest non-decreasing subsequence.
 */
function findLongestNonDecreasingSubsequence(nums) {
    if (nums.length === 0) {
        return [];
    }

    let dp = new Array(nums.length).fill(1);
    let maxLen = 1;
    let maxIndex = 0;

    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] >= nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        if (dp[i] > maxLen) {
            maxLen = dp[i];
            maxIndex = i;
        }
    }

    let longestSubsequence = [];
    longestSubsequence.push(nums[maxIndex]);

    for (let i = maxIndex - 1; i >= 0; i--) {
        if (nums[i] <= longestSubsequence[longestSubsequence.length - 1] && dp[i] === dp[maxIndex] - 1) {
            longestSubsequence.push(nums[i]);
            maxIndex = i;
        }
    }

    return longestSubsequence.reverse();
}
describe('TestAnswer', () => {
    test('non-decreasing sequence', () => {
        const nums = [5, 7, 4, 8, 6, 10, 2, 11];
        const expected = [5, 7, 8, 10, 11];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('all increasing', () => {
        const nums = [1, 2, 3, 4, 5];
        const expected = [1, 2, 3, 4, 5];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('all decreasing', () => {
        const nums = [5, 4, 3, 2, 1];
        const expected = [5];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('single element', () => {
        const nums = [10];
        const expected = [10];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });

    test('empty array', () => {
        const nums = [];
        const expected = [];
        expect(findLongestNonDecreasingSubsequence(nums)).toEqual(expected);
    });
});
