from typing import Dict


def clean_dictionary(input_dict:Dict) -> Dict:
    """
    Cleans the input dictionary by removing keys with invalid values.Valid values are non-NaN, non-None, and non-whitespace strings.

    Args:
        input_dict (Dict): A dictionary to be cleaned.

    Returns:
        Dict: A new dictionary containing only valid values.
    """