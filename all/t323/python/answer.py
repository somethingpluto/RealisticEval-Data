import re


def is_valid_username(username: str) -> bool:
    """
    Verify that a username is valid according to defined criteria.

    :param username: The username to be validated.
    :type username: str
    :returns: True if the username matches the regex pattern, indicating it is valid,
              or False otherwise.
    :rtype: bool
    """
    # Define the regular expression for a valid username
    username_regex = r'^[a-zA-Z0-9_]+$'

    # Test the username against the regular expression
    return bool(re.match(username_regex, username))