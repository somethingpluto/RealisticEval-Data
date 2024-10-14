from typing import Optional, Dict, Any


def deep_merge_objects(obj1: Dict[str, Any], obj2: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Deeply merges two objects.

    If properties are objects in both objects, they are recursively merged.
    If a property exists in both objects but is not an object, the value from obj1 is used.

    Args:
        obj1(Dict[str, Any]): The first object to merge.
        obj2(Optional[Dict[str, Any]]): The second object to merge, which can be None.

    Returns:
        Dict[str, Any]: A new object that is the result of the merge.
    """
