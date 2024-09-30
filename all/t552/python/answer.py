import numpy as np


def are_sets_equal(set1, set2, rtol=1e-5, atol=1e-6):
    """
    Compares two sets of floats for equality within a relative and absolute tolerance.

    Args:
        set1: The first set of floats.
        set2: The second set of floats.
        rtol: The relative tolerance (default: 1e-5).
        atol: The absolute tolerance (default: 1e-6).

    Returns:
        True if the sets are equal within the specified tolerances, False otherwise.
    """
    # Convert sets to sorted lists for comparison
    list1 = sorted(set1)
    list2 = sorted(set2)

    # Check if the lengths of both sets are the same
    if len(list1) != len(list2):
        return False

    # Compare each element in the two sorted lists
    for a, b in zip(list1, list2):
        if not np.isclose(a, b, rtol=rtol, atol=atol):
            return False

    return True
