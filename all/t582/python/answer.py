import urllib.parse


def to_query_string(params: dict) -> str:
    """
    Converts a dictionary to a query string.

    :param params: The parameters to convert.
    :return: The query string.
    """
    query_parts = []
    for key, value in params.items():
        # Check for None (equivalent to null/undefined in TypeScript)
        if value is not None:
            # Encode the key and value, then add to the list
            query_parts.append(f"{urllib.parse.quote(str(key))}={urllib.parse.quote(str(value))}")

    # Join the query parts and return the result
    return '?' + '&'.join(query_parts) if query_parts else ''