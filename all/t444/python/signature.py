def format_comment(string, max_length=60):
    """
    Formats a string into a commented block with specified maximum line length.

    Args:
        string (str): The input string to format.
        max_length (int): Maximum length of each line in the output.

    Returns:
        str: A formatted string with each line prefixed by '# ' and not exceeding the specified max_length.
    """