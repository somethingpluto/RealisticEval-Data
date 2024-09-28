import re


def is_strong_password(password: str) -> bool:
    """
    Check if the provided password is strong.

    A strong password must satisfy the following criteria:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one number
    - At least 8 characters long

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password is strong, False otherwise.
    """
