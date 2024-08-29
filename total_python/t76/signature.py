def remove_common_indentation(multiline_text: str) -> str:
    """
    Removes the common leading indentation from each line in a given multi-line string,
    preserving the relative indentation of the text.

    Args:
        multiline_text (str): The input string containing multiple lines.

    Returns:
        str: The sanitized string with common leading indentation removed.
    """