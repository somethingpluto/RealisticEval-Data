from typing import Dict, List


def sanitize_data(data: Dict, key_to_remove: List = None) -> Dict:
    """
    remove the corresponding sensitive data in the given dictionary based on the given key_to_remove list
    Args:
        data (Dict): original data dict
        key_to_remove (List): key_to_remove list

    Returns:
        removed dict
    """
