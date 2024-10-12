def is_valid_password(password: str) -> bool:
    """
    Checks whether the provided password meets the specified format requirements:
    - At least one number
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one punctuation mark
    - Minimum length of 8 characters

    Args:
        password (str): The password string to validate.

    Returns:
        bool: Returns True if the password meets all requirements; otherwise, False.
    """