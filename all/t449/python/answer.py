import base64

def convert_to_base64(input: str) -> str:
    """
    Converts a string to Base64 encoding.

    Args:
        input (str): The string to be converted to Base64.

    Returns:
        str: The Base64 encoded string.
    """
    # Convert the input string to bytes using UTF-8 encoding
    input_bytes = input.encode('utf-8')
    # Encode the bytes to Base64
    base64_bytes = base64.b64encode(input_bytes)
    # Convert the Base64 bytes back to a string
    return base64_bytes.decode('utf-8')
