def hex_string_to_unsigned_int(hex_string: str) -> int:
    """
    Converts a hexadecimal string to an unsigned integer.

    :param hex_string: The hexadecimal string to be converted.
    :return: An unsigned integer representation of the hexadecimal string.
    """
    return int(hex_string, 16)