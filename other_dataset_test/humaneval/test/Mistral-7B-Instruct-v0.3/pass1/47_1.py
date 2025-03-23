

METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 

def median(l: list):
    """Return median of elements in the list l."""

    # Sort the list
    l.sort()

    # Find the middle element(s)
    n = len(l)
    if n % 2 == 0:
        # Even number of elements
        middle1 = l[n // 2 - 1]
        middle2 = l[n // 2]
        return (middle1 + middle2) / 2
    else:
        # Odd number of elements
        return l[n // 2]
candidate = median
check(candidate)