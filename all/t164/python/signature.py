def uint8_array_to_base64(uint8_array: bytes) -> str:
    """
    The Unit8 array is converted into 4 Base64 characters as a group of 3 bytes for processing,
    and the output of less than 3 is filled with =, and the resulting Base64 string is returned.

    :param uint8_array: The Uint8Array to be converted (as bytes).
    :return: The resulting Base64-encoded string.
    """