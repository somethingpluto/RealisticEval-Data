def merge_objects(obj1: dict, obj2: dict) -> dict:
    """
    Merges two dictionaries into one, with properties from the second dictionary
    potentially overwriting those from the first if there are conflicts.

    Args:
        obj1 (dict): The first dictionary.
        obj2 (dict): The second dictionary.

    Returns:
        dict: The resulting dictionary after merging.
    
    Raises:
        TypeError: If either parameter is not a dictionary or is None.
    """
    if not isinstance(obj1, dict) or obj1 is None or isinstance(obj1, list):
        raise TypeError('Both parameters should be non-null dictionaries and not lists.')
    if not isinstance(obj2, dict) or obj2 is None or isinstance(obj2, list):
        raise TypeError('Both parameters should be non-null dictionaries and not lists.')

    # Merge dictionaries, with obj2 overwriting obj1 in case of conflicts
    merged = {**obj1, **obj2}
    return merged