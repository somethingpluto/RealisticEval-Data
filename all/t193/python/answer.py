def conv_flags(value: int) -> str:
    """
    Invert the flag bits of an unsigned integer to a hexadecimal string.
    
    :param value: The unsigned integer whose bits are to be inverted.
    :return: A string containing the hexadecimal representation of the inverted bits.
    """
    # Create a mask for the first five bits (0x1F = 00011111)
    mask = 0x1F
    
    # Invert the first five bits using XOR
    inverted_value = value ^ mask
    
    # Convert the result to a hexadecimal string
    hex_string = hex(inverted_value)[2:]  # [2:] to remove '0x' prefix
    
    return hex_string
