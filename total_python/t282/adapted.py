def flatten_array(multi_dim_array):
    """
    Flattens a multi-dimensional array into a one-dimensional array.

    Args:
    multi_dim_array (list): A multi-dimensional list (nested list).

    Returns:
    list: A one-dimensional list containing all elements of the input.
    """
    flat_list = []

    def flatten(sub_array):
        for item in sub_array:
            if isinstance(item, list):
                flatten(item)  # Recursively flatten if the current item is a list
            else:
                flat_list.append(item)  # Append the non-list item to the flat_list

    flatten(multi_dim_array)
    return flat_list
