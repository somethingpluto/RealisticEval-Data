class InvalidArgumentError(Exception):
    """Custom exception for invalid arguments."""
    pass


def return_string(s: str) -> str:
    """
    Returns a copy of the specified string.

    :param s: The input string to be copied.
    :return: A copy of the input string.
    :raises InvalidArgumentError: If the input string is None.
    """
    if s is None:
        raise InvalidArgumentError("Input string cannot be null.")

    # Return a copy of the input string
    copied_str = str(s)  # In Python, this creates a copy of the string.
    return copied_str
