/**
 * Find the longest non-decreasing subsequence in the given array.
 *
 * @param {number[]} nums - The input array of integers.
 * @returns {number[]} A list containing the longest non-decreasing subsequence.
 */
function findLongestNonDecreasingSubsequence(nums) {
    if (nums.length === 0) return [];

    // dp[i] will store the length of the longest non-decreasing subsequence ending at index i
    const dp = Array(nums.length).fill(1);
    // prev[i] will store the index of the previous element in the longest non-decreasing subsequence ending at index i
    const prev = Array(nums.length).fill(-1);

    let maxLength = 1;
    let endIndex = 0;

    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] >= nums[j] && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
        if (dp[i] > maxLength) {
            maxLength = dp[i];
            endIndex = i;
        }
    }

    // Reconstruct the longest non-decreasing subsequence
    const result = [];
    while (endIndex !== -1) {
        result.unshift(nums[endIndex]);
        endIndex = prev[endIndex];
    }

    return result;
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
