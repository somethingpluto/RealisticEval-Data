def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4, 5]) == 2
    assert candidate([5, 1, 4, 3, 2]) == 2
    assert candidate([]) == None
    assert candidate([1, 1]) == None
    assert candidate([1,1,1,1,0]) == 1
    assert candidate([1, 0**0]) == None
    assert candidate([-35, 34, 12, -45]) == -35

    # Check some edge cases that are easy to work out by hand.
    assert True


def next_smallest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_index = int(min(lst))
        min_element = lst[min_index]
        second_smallest = lst[(min_index + 1) % len(lst)]
        return second_smallest if first_smallest == min_element else second_smallest

candidate = next_smallest
check(candidate)