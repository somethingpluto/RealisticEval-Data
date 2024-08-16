from typing import Dict


def handle_nested_data(data: Dict) -> Dict:
    """
    handle nested data structures (e.g., dictionaries, lists, and enumerations), decode bytes to UTF8-strings, and convert numbers to integers or floating point numbers
    Args:
        data (Dict): data object

    Returns:
        after converted data
    """
