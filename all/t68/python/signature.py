from typing import List


def divide_list(lst: List, n: int) -> List:
    """
    divide a list evenly into n parts and return a list of these parts. If the list length is not divisible by n, additional elements are added to the previous sections one by one
    Args:
        lst (List): The list to be divided.
        n (int): The number of parts to divide the list into.

    Returns:
        A list containing n sublists, where each sublist represents a part of the original list.
    """
