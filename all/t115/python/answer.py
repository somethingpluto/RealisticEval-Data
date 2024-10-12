def sort_by_key(array, key):
    """
    Sorts a list of dictionaries alphabetically by a specified key.

    :param array: List of dictionaries to be sorted.
    :param key: Key in the dictionaries to sort by.
    :return: The sorted list based on the specified key.
    """
    return sorted(array, key=lambda x: (str(x.get(key, '')).lower()))
