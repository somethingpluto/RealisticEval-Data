from rpds import List


def sort_names(arr: List[str]) -> List[str]:
    """
    Sort a list of strings with the format "name + number" in ascending order.

    If the numbers are the same, the strings are sorted by name in ascending order.

    Args:
        arr (list of str): A reference to the list of strings to be sorted.

    Returns:
        list of str: A list of strings sorted according to the rules described above.
    """