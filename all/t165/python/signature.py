def base64_to_url_safe(base64: str) -> str:
    """
    Converts a standard Base64 encoded string into a URL-safe Base64 encoded string.

    Args:
        base64 (str): The standard Base64 encoded string to be converted.

    Returns:
        str: The URL-safe Base64 encoded string, which replaces '+' with '-' and '/' with '_'
             and may remove any trailing '=' padding.
    """