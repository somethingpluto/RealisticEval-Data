def truncate_string_with_replacement(s: str, max_length: int) -> str:
    """
    Truncate a string to the specified length, replacing the excess part with an ellipsis.

    Args:
        s (str): The string to truncate.
        max_length (int): The maximum length of the resulting string.

    Returns:
        str: The truncated string with ellipsis if applicable.
    """
    # Check if the string length is less than or equal to the specified length
    if len(s) <= max_length:
        return s  # No need to truncate

    # Replace the excess part with ellipsis
    return s[:max_length] + '...'
