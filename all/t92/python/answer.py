import html


def replace_html_entities(html_string: str) -> str:
    """
    Decodes HTML entities in a given HTML string.

    Args:
        html_string (str): The HTML string containing entities to decode.

    Returns:
        str: The decoded string with HTML entities converted back to their original characters.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(html_string, str):
        raise TypeError('Input must be a string.')

    # Use html.unescape to decode HTML entities
    return html.unescape(html_string)