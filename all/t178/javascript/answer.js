/**
 * Finds the longest non-decreasing subsequence in an array of numbers.
 *
 * @param {number[]} nums - An array of numbers.
 * @return {number[]} The longest non-decreasing subsequence.
 */
function findLongestNonDecreasingSubsequence(nums) {
    if (!nums || nums.length === 0) {
        return [];
    }

    const n = nums.length;
    const dp = Array(n).fill(1);  // Initialize dp array with 1s
    const previous = Array(n).fill(-1);  // Initialize previous array with -1s

    let maxLength = 1;
    let lastIndex = 0;

    // Calculate the length of the longest non-decreasing subsequence
    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] >= nums[j] && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
                previous[i] = j;
            }
        }

        // Update maxLength and lastIndex
        if (dp[i] > maxLength) {
            maxLength = dp[i];
            lastIndex = i;
        }
    }

    // Reconstruct the longest non-decreasing subsequence
    const subsequence = [];
    while (lastIndex !== -1) {
        subsequence.unshift(nums[lastIndex]);  // Add to the beginning
        lastIndex = previous[lastIndex];
    }

    return subsequence;
}