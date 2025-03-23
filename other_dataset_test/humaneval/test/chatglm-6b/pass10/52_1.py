

METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10], 100)
    assert not candidate([1, 20, 4, 10], 5)
    assert candidate([1, 20, 4, 10], 21)
    assert candidate([1, 20, 4, 10], 22)
    assert candidate([1, 8, 4, 10], 11)
    assert not candidate([1, 8, 4, 10], 10)

 
def below_threshold(l: list, t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l: List of integers.
        t: Threshold value.

    Returns:
        bool: True if all numbers in the list l are below threshold t, False otherwise.
    """
    # Iterate through the list
    for num in l:
        # Check if num is below threshold t
        if num < t:
            return False
    return True

candidate = below_threshold
check(candidate)