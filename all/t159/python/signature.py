def remove_file_extension(file_name: str) -> str:
    """
    Removes the extension of the given filename and returns the remainder.

    Args:
        file_name (str): The full name of the file from which to remove the extension.

    Returns:
        str: The file name without the extension. If no extension is found, returns the original file name.
    """