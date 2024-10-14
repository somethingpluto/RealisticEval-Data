from typing import List, Any


def compare_arrays(arr1: List[Any], arr2: List[Any]) -> bool:
    """
    Compares two arrays to determine if they contain the same unique elements, irrespective of order.

    Args:
        arr1 (list): The first array to compare. Elements can be of any type T.
        arr2 (list): The second array to compare. Elements should be of the same type as the first array.

    Returns:
        bool: Returns True if both arrays contain the same unique elements, otherwise returns False.

    Template:
        T: The type of the elements in the arrays.
    """