from typing import List, Any, Callable, Dict


def find_matching_elements(arr: List[Any], comparison_fn: Callable[[Any], bool]) -> List[Dict[str, Any]]:
    """
    Finds matching elements and their indices in the input array
    based on the specified comparison function.
    Args:
        arr (str): The input array to search through.
        comparison_fn (): The comparison function to determine matches.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each containing the matched element and its index.
    """
