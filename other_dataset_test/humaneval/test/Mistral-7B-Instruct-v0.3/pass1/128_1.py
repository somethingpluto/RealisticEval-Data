def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1, 2, 2, -4]) == -9
    assert candidate([0, 1]) == 0
    assert candidate([1, 1, 1, 2, 3, -1, 1]) == -10
    assert candidate([]) == None
    assert candidate([2, 4,1, 2, -1, -1, 9]) == 20
    assert candidate([-1, 1, -1, 1]) == 4
    assert candidate([-1, 1, 1, 1]) == -4
    assert candidate([-1, 1, 1, 0]) == 0

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

def prod_signs(arr):
    if not arr:
        return None

    product_of_signs = 1
    sum_of_magnitudes = 0

    for num in arr:
        if num > 0:
            product_of_signs *= 1
        elif num < 0:
            product_of_signs *= -1
        else:
            continue

        sum_of_magnitudes += abs(num)

    return sum_of_magnitudes * product_of_signs
candidate = prod_signs
check(candidate)