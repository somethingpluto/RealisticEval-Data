def get_object_by_id(id, obj_list):
    """
    Returns the object from the list with the given ID, or None if it is not present.

    Args:
        id (str | int): The `id` to search for in the list.
        obj_list (list[dict]): The list of objects to search through.

    Returns:
        dict | None: The object with the matching `id`, or None if no match is found.
    """
    # Iterate over the list of objects
    for obj in obj_list:
        # Check if the object has an `id` key that matches the given id
        if 'id' in obj and obj['id'] == id:
            # If a match is found, return the object
            return obj

    # If no match is found, return None
    return None
