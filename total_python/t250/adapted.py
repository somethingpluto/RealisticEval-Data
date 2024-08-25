def invert_dictionary(original_dict):
    """
    Invert the keys and values in a dictionary. If multiple keys have the same value,
    the new dictionary's values will be a list of these keys.

    Args:
    original_dict (dict): The dictionary to invert.

    Returns:
    dict: A new dictionary with values and keys inverted.
    """
    new_dict = {}
    for key, value in original_dict.items():
        if value not in new_dict:
            new_dict[value] = key
        else:
            # If the value already exists as a key, we need to append to or create a list
            if not isinstance(new_dict[value], list):
                new_dict[value] = [new_dict[value]]
            new_dict[value].append(key)
    return new_dict