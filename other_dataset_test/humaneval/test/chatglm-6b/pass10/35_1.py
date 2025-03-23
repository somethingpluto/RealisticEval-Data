

METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

max_element([1, 2, 3])

max_element(1)

max_element()

max_element([ [1, 2, 3], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10] ])

max_element([ [1, 2, 3], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [4, -2, 11, 6] ])

max_element([ []])

candidate = max_element
check(candidate)