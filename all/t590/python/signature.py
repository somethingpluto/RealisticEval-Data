def parse_http_request_line(response: str) -> dict:
    """
    Parses the first line of an HTTP request.

    Args:
        response (str): The raw HTTP request string.

    Returns:
        dict: A dictionary containing the method, URL, and HTTP version.
    """