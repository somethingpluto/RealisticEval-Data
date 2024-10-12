import re

def compress_html(html):
    """
    Compresses an HTML string by removing unnecessary whitespace,
    including newlines, tabs, and extra spaces,
    while preserving the structure of the HTML.

    Args:
        html (str): The input HTML string to be compressed.

    Returns:
        str: The compressed HTML string with reduced whitespace.
    """
    return (re.sub(r'[\r\n\t]+', '', html)    # Remove all newline and tab characters
            .replace('  ', ' ')              # Replace multiple consecutive spaces with a single space
            .replace('> <', '><')            # Remove spaces between HTML tags
            .strip())                         # Trim any leading and trailing whitespace
