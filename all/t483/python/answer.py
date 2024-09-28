import re


def is_valid_email(email):
    """
    Verifies if the provided string is a valid email address.

    Parameters:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    # Regular expression pattern for validating an email address
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(email_pattern, email):
        return True
    else:
        return False
