def bytes_to_size(bytes: int) -> str:
    """
    Converts a given number of Bytes into a readable string representation
    with the appropriate units (Bytes, KB, MB, GB, or TB) and keeps two decimal places.

    Args:
        bytes (int): The number of bytes to be converted.

    Returns:
        str: A string representation of the size in Bytes, KB, MB, GB, or TB.
    """