def get_cookie(name: str, cookie_string: str) -> str:
    """
    Retrieve the value of a cookie by its name from a cookie string.

    Args:
        name (str): The name of the cookie to retrieve.
        cookie_string (str): The string containing all cookies.

    Returns:
        str: The value of the cookie if found, otherwise None.
    """
    cookie_name = f"{name}="
    cookies = cookie_string.split(';')  # Split the cookie string into individual cookies

    for cookie in cookies:
        cookie = cookie.strip()  # Trim whitespace
        if cookie.startswith(cookie_name):
            return cookie[len(cookie_name):]  # Return the value of the cookie

    return None  # Return None if the cookie is not found