def flatten(nested_list):
    """
    Flattens a nested list into a single list.

    Args:
        nested_list (list): A list that may contain nested lists.

    Returns:
        list: A flattened version of the input list.
    """
    flattened = []  # List to hold the flattened elements
    for element in nested_list:
        if isinstance(element, list):
            # Recursively flatten the nested list and extend the flattened list
            flattened.extend(flatten(element))
        else:
            # If the element is not a list, append it directly
            flattened.append(element)
    return flattened
