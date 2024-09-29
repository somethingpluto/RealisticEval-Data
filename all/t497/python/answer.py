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

    # Initialize out_index with zeros
    for i in range(len(out_index)):
        out_index[i] = 0

    # Calculate the offset to align the shapes
    offset = len(big_shape) - len(shape)

    # Map the big_index to out_index following broadcasting rules
    for i in range(len(shape)):
        # If the current dimension in shape is 1, we set the corresponding out_index to 0
        if shape[i] == 1:
            out_index[i] = 0
        else:
            # Otherwise, use the corresponding value from big_index
            out_index[i] = big_index[i + offset]