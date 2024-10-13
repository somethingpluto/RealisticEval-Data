from typing import Any, Dict


def compare_objects_depth(obj1: Dict[str, Any], obj2: Dict[str, Any]) -> bool:
    """
    Compares two objects to determine if they have the same depth and structure.

    Args:
        obj1: The first object to compare.
        obj2: The second object to compare.

    Returns:
        True if the objects have equal depth, otherwise False.
    """
    # Check if both are dictionaries
    if not isinstance(obj1, dict) or not isinstance(obj2, dict):
        return False

    # Get the keys of both dictionaries
    keys1 = obj1.keys()
    keys2 = obj2.keys()

    # Check if the number of keys is the same
    if len(keys1) != len(keys2):
        return False

    # Compare each key
    for key in keys1:
        # Check if key exists in both dictionaries
        if key not in keys2:
            return False

        # Recursively check the depth of the properties
        is_equal_depth = compare_objects_depth(obj1[key], obj2[key])
        if not is_equal_depth:
            return False

    return True