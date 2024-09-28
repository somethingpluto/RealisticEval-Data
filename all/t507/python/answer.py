import re


def is_strong_password(password):
    """
    Check if the provided password is strong.

    A strong password must satisfy the following criteria:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one number
    - At least 8 characters long

    Parameters:
    password (str): The password to check.

    Returns:
    bool: True if the password is strong, False otherwise.
    """
    # Check password length
    if len(password) < 8:
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one number
    if not re.search(r'\d', password):
        return False

    # If all checks passed, return True
    return True
