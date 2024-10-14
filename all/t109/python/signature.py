from typing import Union, List, Dict, Optional


def get_object_by_id(id: Union[str, int], obj_list: List[Dict]) -> Optional[Dict]:
    """
    Returns the object from the list with the given ID, or None if it is not present.

    Args:
        id (Union[str, int]): The `id` to search for in the list.
        obj_list (List[Dict]): The list of objects to search through.

    Returns:
        Optional[Dict]: The object with the matching `id`, or None if no match is found.
    """