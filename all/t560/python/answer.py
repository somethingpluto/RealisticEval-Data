def get_line_number(content: str, index: int) -> int:
    """
    Gets the line number in the content at the specified index.

    Args:
        content (str): The string content to check.
        index (int): The character index to find the line number for.

    Returns:
        int: The line number corresponding to the given index.
    """
    # Count the number of newline characters before the index
    return content.count('\n', 0, index) + 1