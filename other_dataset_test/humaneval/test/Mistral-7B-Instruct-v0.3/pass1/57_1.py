

METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([4, 1, 1, 0]) == True
    assert candidate([1, 2, 3, 2, 5, 60]) == False
    assert candidate([1, 2, 3, 4, 5, 60]) == True
    assert candidate([9, 9, 9, 9]) == True

def monotonic(l: list):
    direction = l[1] - l[0] > 0
    for i in range(1, len(l) - 1):
        if l[i + 1] - l[i] < 0 if direction else l[i + 1] - l[i] > 0:
            return False
    return True
candidate = monotonic
check(candidate)