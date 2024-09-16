from typing import Dict


def invert_dictionary(original_dict: Dict) -> Dict:
    """
    Invert the keys and values in a dictionary. If multiple keys have the same value,
    the new dictionary's values will be a list of these keys.
    Args:
        original_dict (dict): The dictionary to invert.

    Returns:
        A new dictionary with values and keys inverted.
    """
