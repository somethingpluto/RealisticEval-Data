from typing import List


def convert_to_ring_format(holes: List) -> List:
    """
    Convert a list of hole positions to the ring format (list of 1s and 0s).

    Args:
        holes (list): A list of integers representing the positions of the holes (0-indexed).

    Returns:
        List: A list of length 32, where positions with holes are 0 and others are 1.

    """
