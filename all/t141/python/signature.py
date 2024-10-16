from typing import List, Any


def have_same_unique_elements(array1: List[Any], array2: List[Any]) -> bool:
    """
    Compares two arrays to determine if they contain the same unique elements, irrespective of order.

    Args:
        array1 (List[Any]): The first array to compare. Elements can be of any type.
        array2 (List[Any]): The second array to compare. Elements should be of the same type as the first array.

    Returns:
        bool: Returns True if both arrays contain the same unique elements, otherwise returns False.
    """