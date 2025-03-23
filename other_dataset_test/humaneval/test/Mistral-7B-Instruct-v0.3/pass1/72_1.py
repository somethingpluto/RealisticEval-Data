def check(candidate):

    # Check some simple cases
    assert candidate([3, 2, 3], 9) is True
    assert candidate([1, 2], 5) is False
    assert candidate([3], 5) is True
    assert candidate([3, 2, 3], 1) is False


    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 3], 6) is False
    assert candidate([5], 5) is True

def will_it_fly(q, w):
    if len(q) > 1 and q!= q[::-1]:  # check if the list is not palindromic
        return False

    if sum(q) > w:  # check if the sum of the elements is greater than the maximum possible weight
        return False

    return True
candidate = will_it_fly
check(candidate)