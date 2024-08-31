from typing import List, Union


def find_closest_element(target: Union[int, float], elements: List[Union[int, float]]) -> Union[int, float]:
    """
    Finds and returns the element from the given list that is closest to the specified target value.

    Args:
        target (Union[int, float]): The target number to which we want to find the closest element.
        elements (List[Union[int, float]]): A list of numerical elements from which the closest element is to be found.

    Returns:
        Union[int, float]: The element from the list that is closest to the target value.
    """
