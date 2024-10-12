import re


def is_valid_email(email):
    """
    Check if the given email address is valid.

    :param email: The email address to validate.
    :type email: str
    :returns: True if the email is valid, False otherwise.
    :rtype: bool
    """
    # Define the regular expression for a valid email
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'

    # Test the email against the regular expression
    return bool(re.match(email_regex, email))