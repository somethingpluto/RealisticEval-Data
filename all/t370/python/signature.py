from typing import Tuple


def decompose(n: int, shape: Tuple) -> Tuple:
    """
    Decompose a flat index `n` into a multidimensional index based on the given shape.

    Args:
        n: Flat index (non-negative integer).
        shape: Tuple representing the dimensions of the multi-dimensional array.

    Returns:
        Tuple: Tuple representing the multidimensional index corresponding to `n`.
    Raises:
        ValueError: If `n` is out of bounds for the array defined by `shape`.
    """
