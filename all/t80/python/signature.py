def sanitize_filename(filename: str) -> str:
    """
    remove illegal characters from strings and handle spaces and empty characters to make the modified string comply with windows file name rules

    Args:
        filename (str): The original filename string to be sanitized.

    Returns:
        str: A sanitized string that is safe to use as a Windows filename.
    """
