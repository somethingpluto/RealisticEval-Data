def compress_string(input: str, max_length: int = 18) -> str:
    """
    Compresses a string to ensure its length does not exceed the specified maximum length.
    If the string exceeds the maximum length, it truncates the string and appends an ellipsis ("...").

    :param input: The string to be compressed.
    :param max_length: The maximum allowed length of the string (default is 18).
    :returns: A compressed string that does not exceed the specified length.
    """