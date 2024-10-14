def merge_objects(obj1: dict, obj2: dict) -> dict:
    """
    Merges two dictionaries into one, with properties from the second dictionary
    potentially overwriting those from the first if there are conflicts.

    Args:
        obj1 (dict): The first dictionary.
        obj2 (dict): The second dictionary.

    Returns:
        dict: The resulting dictionary after merging.
    """