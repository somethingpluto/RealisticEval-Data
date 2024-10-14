def safe_splice(input_array:list, amount_to_remove, index_to_remove, replace_with=None):
    """
    Safely splices an array by removing a specified number of elements from a given index,
    and optionally replaces them with a new element.

    Args:
        input_array (list): The original array to be modified.
        amount_to_remove (int): The number of elements to remove from the array.
        index_to_remove (int): The index at which to start removing elements.
        replace_with (any, optional): The element to replace the removed elements with.

    Returns:
        list: A new array with the specified elements removed and optionally replaced.
    """