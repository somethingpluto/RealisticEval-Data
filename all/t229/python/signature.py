def convert_file_size(size_bytes: int) -> str:
    """
    Converts a file size in bytes to a human-readable format.
    For example:
        input: 2120
        output: 2KB
    Args:
        size_bytes (int): The size in bytes to be converted.

    Returns:
        str: The converted size in a human-readable format (e.g., "2KB", "1MB").
    """
