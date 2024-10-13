import re

def is_valid_username(username):
    """
    Checks whether the provided username is valid.
    A valid username is defined as a string that:
    - Has a length between 5 and 16 characters (inclusive).
    - Contains only alphanumeric characters (letters and digits) and spaces.

    Parameters:
    username (str): The username to validate.

    Returns:
    bool: Returns True if the username is valid; otherwise, False.
    """
    
    # Check if the input is a string
    if not isinstance(username, str):
        return False  # Return False if the input is not a string

    # Trim any leading or trailing whitespace from the username
    username = username.strip()

    # Check the length of the username
    length = len(username)
    if length < 5 or length > 16:
        return False  # Return False if length is not within the valid range

    # Check if the username contains only alphanumeric characters and spaces
    is_valid = bool(re.match(r'^[a-zA-Z0-9 ]+$', username))

    return is_valid  # Return True if valid, False otherwise