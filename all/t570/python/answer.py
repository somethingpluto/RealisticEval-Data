from typing import Any, Dict, Optional

PlainObject = Dict[str, Any]

def deep_merge_objects(obj1: PlainObject, obj2: Optional[PlainObject]) -> PlainObject:
    """
    Deeply merges two objects.
    If properties are objects in both objects, they are recursively merged.
    If a property exists in both objects but is not an object, the value from obj1 is used.

    :param obj1: The first object to merge.
    :param obj2: The second object to merge (can be None).
    :returns: A new object that is the result of the merge.
    """
    # Return obj1 if obj2 is None
    if obj2 is None:
        return obj1

    # Create a shallow copy of obj2 to be modified
    output: PlainObject = obj2.copy()

    # Iterate through the keys of obj1
    for key in obj1:
        if key in obj1:  # Check if key exists in obj1
            value1 = obj1[key]
            value2 = obj2.get(key)  # Get the value from obj2, defaults to None if not present

            # Check if both values are dictionaries
            if isinstance(value1, dict) and isinstance(value2, dict):
                # Recursively merge objects
                output[key] = deep_merge_objects(value1, value2)
            else:
                # Use the value from obj1
                output[key] = value1

    return output