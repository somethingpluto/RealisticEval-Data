def compress_string(input: str, max_length: int = 18) -> str:
    """
    Compresses a string to ensure its length does not exceed the specified maximum length.
    If the string exceeds the maximum length, it truncates the string and appends an ellipsis ("...").

    Args:
        input (str): The string to be compressed.
        max_length (int, optional): The maximum allowed length of the string (default is 18).

    Returns:
        str: A compressed string that does not exceed the specified length.
             If truncation occurs, an ellipsis ("...") is appended.
    """