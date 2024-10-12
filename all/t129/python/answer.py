import re

def valid_url(url: str) -> bool:
    """
    Validates a URL string using a simplified and more comprehensive regular expression.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    # Simplified and robust regex for URL validation
    pattern = re.compile(
        r'^(http|https?:\/\/)?' +  # protocol
        r'((([a-zA-Z\d]([a-zA-Z\d-]*[a-zA-Z\d])*)\.)+[a-zA-Z]{2,}|' +  # domain name and extension
        r'((\d{1,3}\.){3}\d{1,3}))' +  # OR IP (v4) address
        r'(:\d+)?' +  # port
        r'(\/[-a-zA-Z\d%_.~+]*)*' +  # path
        r'(\?[;&a-zA-Z\d%_.~+=-]*)?' +  # query string
        r'(\#[-a-zA-Z\d_]*)?$',  # fragment locator
        re.IGNORECASE  # case insensitive matching
    )

    return bool(pattern.match(url))