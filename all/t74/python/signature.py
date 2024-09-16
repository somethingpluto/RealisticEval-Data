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