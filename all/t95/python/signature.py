def find_matching_elements(arr: List[Any], comparison_fn: Callable[[Any], bool]) -> List[Dict[str, Any]]:
    """
    Finds matching elements and their indices in the input array
    based on the specified comparison function.

    :param arr: The input array to search through.
    :param comparison_fn: The comparison function to determine matches.
    :return: A list of dictionaries, each containing the matched element and its index.
    """