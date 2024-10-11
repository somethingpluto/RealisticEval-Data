def sanitize_filename(filename: str) -> str:
    """
    remove illegal characters from windows file path string

    Args:
        filename (str): The original filename string to be sanitized.

    Returns:
        str: A sanitized string that is safe to use as a Windows filename.
    """
