def decompose(n, shape):
    """
    Decompose a flat index `n` into a multidimensional index based on the given shape.

    :param n: Flat index (non-negative integer).
    :param shape: Tuple representing the dimensions of the multi-dimensional array.
    :return: Tuple representing the multidimensional index corresponding to `n`.
    :raises ValueError: If `n` is out of bounds for the array defined by `shape`.
    """
    # Calculate the total size of the array
    size = 1
    for dim in shape:
        size *= dim

    # Check if the index is within bounds
    if not (0 <= n < size):
        raise ValueError("Index out of bounds")

    # Decompose the index
    result = []
    for dim in reversed(shape):
        result.append(n % dim)
        n //= dim  # Update n by integer division

    # Reverse the result to match the original shape order and return as tuple
    return tuple(reversed(result))
