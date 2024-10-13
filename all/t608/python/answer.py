import re


def is_valid_email(email: str) -> bool:
    """Checks whether the given string is a valid email address.

    Args:
        email (str): The string to be checked.

    Returns:
        bool: True if the string is a valid email address, False otherwise.
    """
    if email is None:  # Python uses None instead of null
        return False  # None is not a valid email
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    EMAIL_PATTERN = re.compile(EMAIL_REGEX)
    return bool(EMAIL_PATTERN.match(email))