from typing import List


def remove_triple_backticks(string_list: List[str]) -> List[str]:
    """
    process a list of strings, removing the three consecutive backticks from each string
    Args:
        string_list (List[str]): The list of strings to process.

    Returns:
        A new list with all instances of three consecutive backticks removed from each string.
    """
