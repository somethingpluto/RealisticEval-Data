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
css
nums = [2, 3, 4, 1, 2, 4]
less
[2, 3] = 2 + 3 = 5
[3, 4] = 3 + 4 = 7
[1, 2, 4] = 1 + 2 + 4 = 7

minimum sum of sub-arrays = 5
css
nums = [-1, -2, -3]
less
[-1, -2] = -1 + -2 = 0
[-2, -3] = -2 + -3 = -5
[-1, -2, -3] = -1 + -2 + -3 = -6

minimum sum of sub-arrays = -6

candidate = minSubArraySum
check(candidate)