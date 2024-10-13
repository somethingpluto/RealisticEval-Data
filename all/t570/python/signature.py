def deep_merge_objects(obj1: PlainObject, obj2: Optional[PlainObject]) -> PlainObject:
    """
    Deeply merges two objects.

    If properties are objects in both objects, they are recursively merged.
    If a property exists in both objects but is not an object, the value from obj1 is used.

    Args:
        obj1: The first object to merge.
        obj2: The second object to merge, which can be None.

    Returns:
        A new object that is the result of the merge.
    """