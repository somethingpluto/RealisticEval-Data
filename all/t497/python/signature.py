from typing import List, Tuple

Index = List[int]
Shape = Tuple[int, ...]
OutIndex = List[int]


def broadcast_index(
        big_index: Index,
        big_shape: Shape,
        shape: Shape,
        out_index: OutIndex
) -> None:
    """
    Convert a `big_index` into `big_shape` to a smaller `out_index`
    following broadcasting rules. The `out_index` may be larger or
    have more dimensions than the `shape` given. Additional dimensions
    may need to be mapped to 0 or removed.

    Args:
        big_index (Index): Multidimensional index of the larger tensor.
        big_shape (Shape): Shape of the larger tensor.
        shape (Shape): Shape of the smaller tensor.
        out_index (OutIndex): Multidimensional index of the smaller tensor.

    Returns:
        None: The function modifies `out_index` in place.
    """