from dataclasses import is_dataclass
from typing import Any, Dict

def class_to_dict(obj: Any) -> Dict[str, Any]:
    """
    Converts a dataclass or class instance to a dictionary.

    Args:
        obj: An instance of a dataclass or a class.

    Returns:
        A dictionary representation of the class or dataclass.
    """
    if is_dataclass(obj):
        return obj.__dict__
    elif isinstance(obj, type):
        return {k: v for k, v in obj.__dict__.items() if not k.startswith("__")}
    else:
        return obj.__dict__ if hasattr(obj, '__dict__') else {}
