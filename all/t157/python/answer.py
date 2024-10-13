def bytes_to_size(bytes: int) -> str:
    """
    Converts a given number of Bytes into a readable string representation
    with the appropriate units (Bytes, KB, MB, GB, or TB) and keeps two decimal places.

    Args:
        bytes (int): The number of bytes to be converted.

    Returns:
        str: A string representation of the size in Bytes, KB, MB, GB, or TB.
    """
    # Define the size units array
    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']

    # Return '0 Byte' if the input is zero
    if bytes == 0:
        return '0 Byte'

    # Calculate the index for the size unit and the converted size
    i = int(bytes).bit_length() // 10 if bytes > 0 else 0
    size = bytes / (1024 ** i)

    # Return the size with the appropriate unit formatted to two decimal places
    return f"{size:.2f} {sizes[i]}"
