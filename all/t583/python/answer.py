from urllib.parse import urlparse, urlunparse, parse_qs, urlencode


def remove_query_param(url: str, key: str) -> str:
    """
    Removes the specified parameter from the URL query string.

    :param url: The URL from which to remove the parameter.
    :param key: The key of the parameter to remove.
    :return: The modified URL with the specified parameter removed.
    """
    # Parse the URL into its components
    url_parts = list(urlparse(url))

    # Parse the query parameters into a dictionary
    query_params = parse_qs(url_parts[4])

    # Remove the specified key if it exists
    if key in query_params:
        del query_params[key]

    # Rebuild the query string from the remaining parameters
    url_parts[4] = urlencode(query_params, doseq=True)

    # Return the modified URL
    return urlunparse(url_parts)
