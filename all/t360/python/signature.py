def get_last_part_of_filepath(file_path: str) -> str:
    """
    Extract the last part of a complete file path using a separator.

    If no separator is found, the original string is returned.

    Args:
        file_path (str): The complete file path as a string.

    Returns:
        str: The last part of the file path after the last separator, or the original string if no separator is found.
    """