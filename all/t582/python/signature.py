def to_query_string(params: dict) -> str:
    """
    Converts a dictionary of parameters to a query string.

    For example:
        - Input: {'search': 'test', 'page': 1, 'size': 10}
        - Output: '?search=test&page=1&size=10'

    Args:
        params (dict): The parameters to convert. The keys should be strings
                       and values can be of any type that can be converted to a string.

    Returns:
        str: The query string representation of the parameters.
    """