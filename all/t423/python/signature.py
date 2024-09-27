def write_unique_line_to_file(filename: str, line_content: str):
    """
    Writes a line to a text file only if the line with the same content does not already exist.

    Args:
        filename (str): The name of the file to write to.
        line_content (str): The content of the line to write.

    Returns:
        None
    """