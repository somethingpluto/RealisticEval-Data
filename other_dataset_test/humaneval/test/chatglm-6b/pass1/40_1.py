

METADATA = {}


def check(candidate):
    assert candidate([1, 3, 5, 0]) == False
    assert candidate([1, 3, 5, -1]) == False
    assert candidate([1, 3, -2, 1]) == True
    assert candidate([1, 2, 3, 7]) == False
    assert candidate([1, 2, 5, 7]) == False
    assert candidate([2, 4, -5, 3, 9, 7]) == True
    assert candidate([1]) == False
    assert candidate([1, 3, 5, -100]) == False
    assert candidate([100, 3, 5, -100]) == False


[1, 3, 5, 0]

[1, 3, -2, 1]

[1, 2, 3, 7]

[2, 4, -5, 3, 9, 7]

[1]

[1, 0, 0, 0]

candidate = triples_sum_to_zero
check(candidate)