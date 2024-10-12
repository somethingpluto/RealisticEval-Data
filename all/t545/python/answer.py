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
    result = []  # Initialize an empty list to hold the result
    for element in array:
        if element is None:  # Exit the loop if None is encountered
            break
        result.append(element)  # Add the current element to the result list
    return result  # Return the result list