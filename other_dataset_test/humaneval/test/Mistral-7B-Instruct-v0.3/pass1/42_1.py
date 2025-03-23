

METADATA = {}


def check(candidate):
    assert candidate([]) == []
    assert candidate([3, 2, 1]) == [4, 3, 2]
    assert candidate([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124]

def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i + 1 for i in enumerate(l)[0]]
candidate = incr_list
check(candidate)