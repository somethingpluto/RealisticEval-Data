def sort_by_field(array, field, ascending=True):
    """
    Sorts a list of dictionaries alphabetically based on a specified field.

    Args:
        array (list): The list of dictionaries to sort.
        field (str): The field of the dictionaries to sort by.
        ascending (bool): If True, sort in ascending order; if False, sort in descending order.

    Returns:
        list: The sorted list of dictionaries.

    Raises:
        ValueError: If the field does not exist in the dictionaries.
    """
    # Check if the array is empty or if the field exists in the first dictionary
    if not array or field not in array[0]:
        raise ValueError('Field does not exist in the objects.')

    # Sorting function
    return sorted(
        array,
        key=lambda x: x[field].lower(),
        reverse=not ascending  # If ascending is False, reverse the sort order
    )