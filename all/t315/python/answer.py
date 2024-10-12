from urllib.parse import urlparse, parse_qs, unquote

def get_file_id_from_url(url: str) -> str:
    """Extract the file ID from the given URL query args.

    Args:
        url (str): The URL from which the file ID is to be extracted.

    Returns:
        str: The extracted file ID if present, otherwise None if the URL does not conform to the expected format.
    """
    try:
        # Parse the URL
        parsed_url = urlparse(url)
        # Extract query parameters
        query_params = parse_qs(parsed_url.query)
        # Get the file ID from the query parameters, unquoting if necessary
        file_id = query_params.get('fileId', [None])[0]
        return unquote(file_id) if file_id else None
    except Exception as error:
        print('Invalid URL:', error)
        return None  # Return None if the URL is invalid or an error occurs.
