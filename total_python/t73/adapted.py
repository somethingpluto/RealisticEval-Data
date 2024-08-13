def dict_of_lists_to_list_of_dicts(dict_of_lists):
    """
    Convert a dictionary of lists into a list of dictionaries.

    Args:
    dict_of_lists (dict): A dictionary where each key has a list as its value.

    Returns:
    list of dicts: A list where each item is a dictionary formed by corresponding elements of lists in the input dictionary.

    Raises:
    ValueError: If lists in the dictionary are of different lengths.
    """
    # Check if all lists are of the same length
    if len(dict_of_lists) == 0:
        return []
    if len(set(len(lst) for lst in dict_of_lists.values())) != 1:
        raise ValueError("All lists in the dictionary must have the same length.")

    # Using zip to iterate over lists simultaneously
    keys = dict_of_lists.keys()
    list_of_dicts = [dict(zip(keys, values)) for values in zip(*dict_of_lists.values())]

    return list_of_dicts
