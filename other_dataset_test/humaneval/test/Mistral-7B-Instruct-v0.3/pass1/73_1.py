def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3,5,4,7,9,6]) == 4
    assert candidate([1, 2, 3, 4, 3, 2, 2]) == 1
    assert candidate([1, 4, 2]) == 1
    assert candidate([1, 4, 4, 2]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 3, 2, 1]) == 0
    assert candidate([3, 1, 1, 3]) == 0
    assert candidate([1]) == 0
    assert candidate([0, 1]) == 1

def smallest_change(arr):
    n = len(arr)
    arr.sort()

    # Calculate the difference between the sorted index and the original index for each element
    diff = [i - arr.index(arr[i]) for i in range(n)]

    # Make changes to make the array palindromic
    changes = 0
    for i in range(n // 2):
        # Find the maximum possible change we can make
        max_change = min(diff[i], diff[n - i - 1])
        changes += max_change

        # Update the differences
        diff[i] -= max_change
        diff[n - i - 1] -= max_change

    # If there are any remaining differences, we can't make the array palindromic
    if any(diff):
        return -1

    return changes
candidate = smallest_change
check(candidate)