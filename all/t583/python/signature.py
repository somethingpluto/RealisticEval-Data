def remove_query_param(url: str, key: str) -> str:
    """
    Removes the specified parameter from the URL query string.

    This function parses the URL, removes the specified query parameter,
    and returns the modified URL. If the parameter does not exist,
    the original URL is returned.

    For example:
        - Input: 'http://example.com/page?search=test&page=1', 'search'
        - Output: 'http://example.com/page?page=1'

    Args:
        url (str): The URL from which to remove the parameter.
        key (str): The key of the parameter to remove.

    Returns:
        str: The modified URL with the specified parameter removed.
    """