def safe_splice(input_array, amount_to_remove, index_to_remove, replace_with=None):
    """
    Safely removes elements from the input array and optionally replaces
    the removed elements with a new value.

    Args:
        input_array (list): The original list from which elements are removed.
        amount_to_remove (int): The number of elements to remove.
        index_to_remove (int): The starting index from which to remove elements.
        replace_with (any, optional): The value to insert in place of the removed elements.

    Returns:
        list: A new list after removal and optional replacement.
    """
    before = input_array[:index_to_remove]  # Elements before the index
    after = input_array[index_to_remove + amount_to_remove:]  # Elements after the removed section

    if replace_with is not None:
        before.append(replace_with)  # Append the replacement value if provided

    return before + after  # Concatenate the two lists
