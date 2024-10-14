def filter_array(unfiltered_array: list, is_qualified: callable) -> list:
    """
    Filters elements from an array based on a qualification function.

    Args:
        unfiltered_array (list): The array to filter.
        is_qualified (callable): A function that determines if an element qualifies.

    Returns:
        list: A new list containing the elements that qualify.
    """