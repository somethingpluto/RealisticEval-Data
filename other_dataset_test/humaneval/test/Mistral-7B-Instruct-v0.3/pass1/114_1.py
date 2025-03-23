def check(candidate):

    # Check some simple cases
    assert candidate([2, 3, 4, 1, 2, 4]) == 1, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([-1, -2, -3]) == -6
    assert candidate([-1, -2, -3, 2, -10]) == -14
    assert candidate([-9999999999999999]) == -9999999999999999
    assert candidate([0, 10, 20, 1000000]) == 0
    assert candidate([-1, -2, -3, 10, -5]) == -6
    assert candidate([100, -1, -2, -3, 10, -5]) == -6
    assert candidate([10, 11, 13, 8, 3, 4]) == 3
    assert candidate([100, -33, 32, -1, 0, -2]) == -33

    # Check some edge cases that are easy to work out by hand.
    assert candidate([-10]) == -10, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([7]) == 7
    assert candidate([1, -1]) == -1
def minSubArraySum(nums):
    if not nums:
        return 0

    min_sum = float('inf')
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        while current_sum > 0 and current_sum > min_sum:
            current_sum -= nums[i - 1]
            i -= 1

        min_sum = min(min_sum, current_sum)

    return min_sum
candidate = minSubArraySum
check(candidate)