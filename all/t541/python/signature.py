def filter_array(unfiltered_array: list, is_qualified: callable) -> list:
    """
    Filters elements from an array based on a qualification function.

    :param unfiltered_array: The array to filter.
    :param is_qualified: The function that determines if an element qualifies.
    :return: A new list containing the elements that qualify.
    """