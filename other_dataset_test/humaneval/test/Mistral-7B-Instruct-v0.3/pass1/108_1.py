def check(candidate):

    # Check some simple cases
    assert candidate([]) == 0
    assert candidate([-1, -2, 0]) == 0
    assert candidate([1, 1, 2, -2, 3, 4, 5]) == 6
    assert candidate([1, 6, 9, -6, 0, 1, 5]) == 5
    assert candidate([1, 100, 98, -7, 1, -1]) == 4
    assert candidate([12, 23, 34, -45, -56, 0]) == 5
    assert candidate([-0, 1**0]) == 1
    assert candidate([1]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

def count_nums(arr):
    counter = 0
    for num in arr:
        if num < 0:
            num = abs(num)
            digits = list(str(num))
            num = sum(map(int, digits))
        else:
            digits = list(str(num))
            num = sum(digits)
        if num > 0:
            counter += 1
    return counter
candidate = count_nums
check(candidate)