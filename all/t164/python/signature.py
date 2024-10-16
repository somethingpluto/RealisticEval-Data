def uint8_array_to_base64(uint8_array: bytes) -> str:
    """
    Converts a Uint8Array (or bytes) into a Base64-encoded string.
    The conversion processes the input in groups of 3 bytes,
    resulting in 4 Base64 characters. If the output is less than 3 bytes,
    the result is padded with '=' characters.

    Args:
        uint8_array (bytes): The Uint8Array to be converted (as bytes).

    Returns:
        str: The resulting Base64-encoded string, which may include '=' padding
             if the input length is not a multiple of 3.
    """
