def base64_to_url_safe(base64: str) -> str:
    """
    Converts a standard Base64 encoded string into a URL-safe Base64 encoded string.

    :param base64: The standard Base64 encoded string to be converted.
    :return: The URL-safe Base64 encoded string.
    """
    # Replace "+" with "-", "/" with "_", and remove trailing "=" characters
    url_safe_base64 = (
        base64.replace("+", "-")  # Replace all occurrences of "+" with "-"
        .replace("/", "_")        # Replace all occurrences of "/" with "_"
        .rstrip("=")              # Remove any trailing "=" characters
    )
    return url_safe_base64
