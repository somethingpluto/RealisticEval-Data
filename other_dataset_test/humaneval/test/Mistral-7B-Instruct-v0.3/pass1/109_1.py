def check(candidate):

    # Check some simple cases
    assert candidate([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([3, 5, 10, 1, 2])==True
    assert candidate([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert candidate([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([])==True
def move_one_ball(arr):
    if not arr:
        return True
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] > 1:
            return False
    return True if min(arr) < max(arr) and (max(arr) - min(arr)) in arr else False
candidate = move_one_ball
check(candidate)