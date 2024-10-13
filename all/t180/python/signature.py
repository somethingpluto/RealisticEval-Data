from typing import List


def binary_search_closest(array: List[int], target: int) -> int:
    """
    Performs a binary search to find the index of the target value in a sorted array.
    If the target value is not found, it returns the index of the closest value.

    Args:
        array (List[int]): The sorted array in which to search.The sorted array in which to search.
        target (int): The target value to search for.

    Returns:
        int: The index of the target or the index of the closest value if the target is not found.
    """
