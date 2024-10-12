def is_valid_username(username: str) -> bool:
    """
    Verify that a string is a valid username and check that the username contains only letters, numbers, and underscores.

    :param username: The username to be validated.
    :type username: str
    :returns: True if the username matches the regex pattern, indicating it is valid;
              False if the username contains any characters outside of letters, numbers, and underscores.
    :rtype: bool
    """