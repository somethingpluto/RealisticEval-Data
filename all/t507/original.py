def is_strong_password(password: str) -> bool:
    """
    Checks if a password is strong enough, ie.
    it has at least 8 characters, at least one lower and one upper case and at least one number.
    :param password: The password to check
    :return: If it is strong enough or not
    """
    
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    return bool(pattern.match(password))