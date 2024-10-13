def hex_string_to_byte_array(hex_str: str) -> bytes:
    """Converts a hexadecimal string into a byte array. Hexadecimal strings are often used to represent binary data
    in a readable format, especially in networking, cryptography, and systems programming.

    Args:
        hex_str (str): The hexadecimal string to be converted. This string should only contain hexadecimal characters
                       (0-9, A-F, a-f). If the string has an odd number of characters, a leading zero is added to ensure
                       proper conversion.

    Returns:
        bytes: A byte array representing the binary data encoded in the hex string.
    """