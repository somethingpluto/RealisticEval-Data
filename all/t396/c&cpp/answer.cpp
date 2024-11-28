#include <iostream>
#include <vector>
#include <algorithm>

int length_of_LIS(const std::vector<int>& nums) {
    /**
     * Given a vector of integers nums, find the length of the longest strictly increasing subsequence in it.
     *
     * Args:
     *     nums (std::vector<int>): Integer vector.
     *
     * Returns:
     *     int: Length of the longest strictly increasing subsequence.
     */
    if (nums.empty()) {
        return 0;
    }

    std::vector<int> dp(nums.size(), 1);

    for (size_t i = 0; i < nums.size(); ++i) {
        for (size_t j = 0; j < i; ++j) {
            if (nums[i] > nums[j]) {
                dp[i] = std::max(dp[i], dp[j] + 1);
            }
        }
    }

    return *std::max_element(dp.begin(), dp.end());
}