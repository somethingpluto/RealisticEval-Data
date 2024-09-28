def compute_output_index(idx_1: int, idx_2: int) -> int:
    """
    Computes the output index from two given indices in the MultiVector's representation
    of the G_n orthonormal basis.

    This function interprets the integers as little-endian bitstrings, takes their XOR,
    and interprets the result as an integer in little-endian.

    Args:
        idx_1 (int): Input index 1.
        idx_2 (int): Input index 2.

    Returns:
        int: The computed output index.
    """
    # Perform bitwise XOR between the two indices
    result = idx_1 ^ idx_2

    # Convert result to little-endian byte representation
    result_bytes = result.to_bytes((result.bit_length() + 7) // 8, byteorder='little')

    # Convert little-endian bytes back to an integer
    result_int = int.from_bytes(result_bytes, byteorder='little')

    return result_int
