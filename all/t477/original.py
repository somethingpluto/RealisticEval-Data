from dataclasses import is_dataclass
from typing import Any


def can_class_to_dict(obj) -> bool:
    """Can we treat this as a dict"""
    if is_dataclass(obj):
        return True
    if isinstance(obj, type):
        return True
    if hasattr(obj, "__dict__"):
        return True
    return False