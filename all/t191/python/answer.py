import struct

def float_to_hex(value: float) -> str:
    """
    Converts a float to its hexadecimal string representation.
    
    :param value: The float value to convert.
    :return: The hexadecimal representation of the float as a string.
    """
    # Interpret the float's bit pattern as an unsigned integer
    int_representation = struct.unpack('!I', struct.pack('!f', value))[0]
    
    # Convert the unsigned integer to a hexadecimal string
    hex_string = f"{int_representation:08x}"
    
    return hex_string