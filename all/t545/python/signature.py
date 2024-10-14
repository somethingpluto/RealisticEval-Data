from typing import List, Any


def elements_before_null(array: List[Any]) -> List[Any]:
    """
    Iterates through the array of elements until the first None is encountered,
    returning a new list that includes all elements before None.

    Args:
        array (List[Any]): The array to iterate through.

    Returns:
        List[Any]: A new list containing elements before the first None.
    """