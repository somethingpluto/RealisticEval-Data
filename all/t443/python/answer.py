def compress_whitespace(input_string):
    """
    Compress multiple consecutive whitespace characters in a string into a single space.

    Parameters:
    input_string (str): The string to be processed.

    Returns:
    str: The processed string with compressed whitespace.
    """
    # Split the input string by whitespace and join with a single space
    return ' '.join(input_string.split())
