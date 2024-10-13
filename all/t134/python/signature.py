import re


def is_valid_username(username: str) -> bool:
    """
    Checks whether the provided username is valid.
    A valid username is defined as a string that:
    - Has a length between 5 and 16 characters (inclusive).
    - Contains only alphanumeric characters (letters and digits) and spaces.

    Args:
        username (str): The username to validate.

    Returns:
        bool: Returns True if the username is valid; otherwise, False.
    """
