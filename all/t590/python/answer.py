def parse_http_request_line(response: str) -> dict:
    """
    Parses the first line of an HTTP request.

    Args:
        response (str): The raw HTTP request string.

    Returns:
        dict: A dictionary containing the method, URL, and HTTP version.
    """
    # Initialize the result dictionary
    result = {}

    # Step 1: Find the position of the first line of the response (request line)
    end_of_first_line = response.find("\r\n")
    if end_of_first_line == -1:
        # If no valid line break is found, return an empty dictionary
        return result

    # Step 2: Extract the first line (the request line)
    request_line = response[:end_of_first_line]

    # Step 3: Split the request line into method, URL, and version
    parts = request_line.split()

    if len(parts) < 3:
        # If there are not enough parts, return an empty dictionary
        return result

    method = parts[0]        # Parse method (e.g., GET, POST)
    url = parts[1]           # Parse URL (e.g., /index.html)
    http_version = parts[2]  # Parse HTTP version (e.g., HTTP/1.1)

    # Step 4: Store the parsed information in the result dictionary
    result["method"] = method
    result["url"] = url
    result["http_version"] = http_version

    # Step 5: Return the result dictionary
    return result