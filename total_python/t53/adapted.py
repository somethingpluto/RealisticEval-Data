import sys


def size_in_bytes(obj):
    """
    Computes and returns the size of an object in bytes.

    Args:
    obj (any): The object to measure the memory size of.

    Returns:
    int: The size of the object in bytes.
    """
    return sys.getsizeof(obj)