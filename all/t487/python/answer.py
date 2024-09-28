import re


def contains_email(text: str) -> bool:
    """
    Check if the given text contains an email address.

    Args:
    text (str): The string to search for an email address.

    Returns:
    bool: True if an email address is found, False otherwise.
    """
    # Define a regex pattern for validating an email address
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Search for the email pattern in the text
    if re.search(email_pattern, text):
        return True
    return False