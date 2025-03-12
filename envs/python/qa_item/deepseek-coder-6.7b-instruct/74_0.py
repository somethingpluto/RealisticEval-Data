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
    if bit_length not in [32, 64]:
        return None

    # Determine the format string for struct.pack
    format_string = 'f' if bit_length == 32 else 'd'

    # Pack the decimal value into a binary format
    packed_value = struct.pack(format_string, decimal_value)

    # Convert the packed binary value to an integer
    int_value = int.from_bytes(packed_value, byteorder='big')

    # Convert the integer to a binary string and strip the '0b' prefix
    binary_string = bin(int_value)[2:]

    # Pad the binary string to the correct bit length
    padded_binary_string = binary_string.zfill(bit_length)

    return padded_binary_string
import unittest


class TestConvertDecimalToBinary(unittest.TestCase):
    def test_basic_32_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(3.14, 32),
                         '01000000010010001111010111000011',
                         "3.14 should be correctly converted to 32-bit binary")

    def test_basic_64_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(3.14, 64),
                         '0100000000001001000111101011100001010001111010111000010100011111',
                         "3.14 should be correctly converted to 64-bit binary")

    def test_advance_32_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(1.5, 32), '00111111110000000000000000000000',
                         "1.5 should be correctly converted to 32-bit binary")

    def test_advance_64_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(1.5, 64),
                         '0011111111111000000000000000000000000000000000000000000000000000',
                         "1.5 should be correctly converted to 32-bit binary")

if __name__ == '__main__':
    unittest.main()