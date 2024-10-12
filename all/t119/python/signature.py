def get_cookie(name: str) -> str:
    """
    Gets the cookie value for the specified name from the cookie string.

    The format of the cookie is key=value; key=value; key=value.

    Args:
        name (str): The name of the cookie key to retrieve.

    Returns:
        str: The value of the specified cookie if found; otherwise, None.
    """
