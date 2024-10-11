import struct
from typing import Union

def convert_decimal_to_binary(decimal_value: float, bit_length: int) -> Union[str, None]:
    """
    Converts a decimal number to its binary representation in either 32-bit or 64-bit format.

    Args:
        decimal_value (float): The decimal number to convert.
        bit_length (int): The desired bit length for the binary representation (32 or 64).

    Returns:
        Union[str, None]: The binary string representation of the decimal number if the bit length
                          is valid, otherwise `None`.
    """
    if bit_length == 32:
        # Convert the decimal to a 32-bit binary representation
        packed_value = struct.pack('>f', decimal_value)
        unpacked_value = struct.unpack('>l', packed_value)[0]
        binary_representation = bin(unpacked_value & 0xffffffff)[2:].zfill(32)
    elif bit_length == 64:
        # Convert the decimal to a 64-bit binary representation
        packed_value = struct.pack('>d', decimal_value)
        unpacked_value = struct.unpack('>q', packed_value)[0]
        binary_representation = bin(unpacked_value & 0xffffffffffffffff)[2:].zfill(64)
    else:
        raise ValueError("Invalid bit length. Please specify either 32 or 64.")

    return binary_representation

