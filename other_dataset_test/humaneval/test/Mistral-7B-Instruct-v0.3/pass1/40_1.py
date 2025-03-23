

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

def triples_sum_to_zero(l):
    if len(l) < 3:
        return False

    numbers = set(l)
    for num1 in numbers:
        for num2 in numbers:
            if num1 + num2 in numbers:
                return True
    return False
candidate = triples_sum_to_zero
check(candidate)