def compress_string(input: str, max_length: int = 18) -> str:
    """
    Compresses a string to ensure its length does not exceed the specified maximum length.
    If the string exceeds the maximum length, it truncates the string and appends an ellipsis ("...").

    :param input: The string to be compressed.
    :param max_length: The maximum allowed length of the string (default is 18).
    :returns: A compressed string that does not exceed the specified length.
    """
    # Check if the input string exceeds the maximum length
    if len(input) > max_length:
        # Truncate the string to the maximum length minus 3 for the ellipsis
        truncated_string = input[:max_length - 3]
        return truncated_string + '...'  # Append ellipsis

    return input  # Return the original string if it's within the length limit
