def get_last_part_of_filepath(file_path: str) -> str:
    """
    Extracts the last part of a complete file path with the help of a separator and returns it,
    or the original string if no separator is found.

    This function extracts the last part of a file path after the last occurrence of the specified
    separator. If the separator is not found in the path, the function returns the original string.

    :param file_path: The complete file path as a string.
    :return: The last part of the file path after the last separator, or the original string if no separator is found.
    """
    pos = max(file_path.rfind('/'), file_path.rfind('\\'))  # Find last occurrence of '/' or '\'
    if pos == -1:  # If no separator found
        return file_path  # Return the original string if no separator is found
    return file_path[pos + 1:]  # Return the substring after the last separator
