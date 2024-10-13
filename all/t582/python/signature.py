def to_query_string(params: dict) -> str:
    """
    Converts an object to a query string.

    For example:
        input: { 'search': 'test', 'page': 1, 'size': 10 }
        output: '?search=test&page=1&size=10'

    :param params: The parameters to convert.
    :type params: dict
    :return: The query string.
    :rtype: str
    """