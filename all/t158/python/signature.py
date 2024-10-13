def get_file_extension(file_name: str) -> str:
    """
    Extract the file extension and return it if it exists. If not, an empty string is returned.

    Args:
        file_name (str): The full name of the file from which to extract the extension.

    Returns:
        str: The file extension without the dot, or an empty string if no extension is found.
    """