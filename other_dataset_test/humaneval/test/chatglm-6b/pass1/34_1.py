

METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


def unique(l: list) -> list:
    return sorted(l)

candidate = unique
check(candidate)