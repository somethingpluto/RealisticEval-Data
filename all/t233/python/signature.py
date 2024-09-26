def remove_comments(string: str) -> str:
    """
    Removes comments from the provided string. Comments start with a '#' and end at the newline.
    For example:
        input: Hello, world! # This is a comment
        output:  Hello, world!
    Args:
        string (str): The input string containing potential comments.

    Returns:
        str: The string with all comments removed.
    """
