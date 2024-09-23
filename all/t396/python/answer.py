from typing import List


def length_of_LIS(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the length of the longest strictly increasing subsequence in it

    Args:
        nums (List[int]): int array

    Returns:
        int: longest strictly increasing subsequence
    """
    if not nums:
        return 0
    dp = []
    for i in range(len(nums)):
        dp.append(1)
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
