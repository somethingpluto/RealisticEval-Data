

METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


def median(l: list) -> float:
    if len(l) <= 1:
        return l[0]
    else:
        return (l[-1] + l[-2]) / 2.0

candidate = median
check(candidate)