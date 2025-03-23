

METADATA = {}


def check(candidate):
    assert candidate([]) == []
    assert candidate([3, 2, 1]) == [4, 3, 2]
    assert candidate([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124]


def incr_list(l: list) -> list:
    """Return list with elements incremented by 1.
    
    Parameters:
        l (list): List to increment.
    
    Returns:
        List with elements incremented by 1.
    
    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
    """
    return list(map(lambda x: x + 1, l))

candidate = incr_list
check(candidate)