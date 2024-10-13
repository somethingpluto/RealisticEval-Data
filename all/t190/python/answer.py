import struct

def hex_string_to_float(hex_str: str) -> float:
    """
    Converts a hexadecimal string to a floating-point number.

    :param hex_str: A string representing the hexadecimal value.
    :return: The floating-point number represented by the hexadecimal string.
    """
    # Convert hexadecimal string to an integer
    int_value = int(hex_str, 16)

    # Convert integer to bytes (4 bytes for a float)
    byte_value = int_value.to_bytes(4, byteorder='little')

    # Unpack bytes into a float
    float_value = struct.unpack('f', byte_value)[0]

    return float_value