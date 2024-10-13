def remove_file_extension(file_name: str) -> str:
    """
    Removes the extension of the given filename and returns the remainder.

    Args:
        file_name (str): The full name of the file from which to remove the extension.

    Returns:
        str: The file name without the extension. If no extension is found, returns the original file name.
    """
    # Find the index of the last dot in the file name
    last_dot_index = file_name.rfind('.')

    # If a dot is found and it is not the first character
    if last_dot_index != -1:
        # Return the substring from the beginning to the last dot
        return file_name[:last_dot_index]

    # Return the original file name if no dot is found
    return file_name