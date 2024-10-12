def get_file_id_from_url(url: str) -> str:
    """Extract the file ID from the given URL query args.

    If not found, return None.

    Args:
        url (str): The URL from which the file ID is to be extracted.

    Returns:
        str: The extracted file ID if present, otherwise None if the URL does not conform to the expected format.

    Example:
        Input: "https://example.com/download?fileId=12345"
        Output: "12345"
    """