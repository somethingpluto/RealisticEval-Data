from typing import Dict, List


def dict_of_lists_to_list_of_dicts(dict_of_lists: Dict) -> List[Dict]:
    """
    Convert a dictionary of lists into a list of dictionaries.
    Args:
        dict_of_lists (dict): A dictionary where each key has a list as its value.

    Returns:
        list of dicts: A list where each item is a dictionary formed by corresponding elements of lists in the input dictionary.
    """
