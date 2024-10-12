import re


def is_valid_password(password: str) -> bool:
    """
    Checks whether the provided password meets the specified format requirements:
    - At least one number
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one punctuation mark
    - Minimum length of 8 characters

    Args:
        password (str): The password string to validate

    Returns:
        bool: Returns True if the password meets all requirements; otherwise, False.
    """
    # Regular expression patterns for the required criteria
    has_number = re.compile(r'[0-9]')  # At least one number
    has_lowercase = re.compile(r'[a-z]')  # At least one lowercase letter
    has_uppercase = re.compile(r'[A-Z]')  # At least one uppercase letter
    has_punctuation = re.compile(r'[!@#$%^&*(),.?":{}|<>]')  # At least one punctuation mark
    has_minimum_length = re.compile(r'.{8,}')  # At least 8 characters

    # Check each condition
    is_valid = (has_number.search(password) and
                has_lowercase.search(password) and
                has_uppercase.search(password) and
                has_punctuation.search(password) and
                has_minimum_length.search(password))

    return is_valid
