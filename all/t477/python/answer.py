from dataclasses import is_dataclass
from typing import Any

def can_class_to_dict(obj: Any) -> bool:
    """
    Check if the given object can be treated as a dictionary.

    Args:
        obj (Any): any type

    Returns:
        bool: can obj to dict
    """
    return is_dataclass(obj) or isinstance(obj, type) or hasattr(obj, "__dict__")