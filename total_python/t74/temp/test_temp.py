import unittest

class TestConvertDecimalToBinary(unittest.TestCase):
    def test_invalid_bit_length(self):
        with self.assertRaises(ValueError):
            convert_decimal_to_binary(3.14, 16)  # Invalid bit length, should raise ValueError

    def test_basic_32_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(3.14, 32),
                         '01000000010010001111010111000011',
                         "3.14 should be correctly converted to 32-bit binary")

    def test_basic_64_bit_conversion(self):
        self.assertEqual(convert_decimal_to_binary(3.14, 64),
                         '0100000000001001000111101011100001010001111010111000010100011111',
                         "3.14 should be correctly converted to 64-bit binary")

    def test_32_bit_edge_case(self):
        self.assertEqual(convert_decimal_to_binary(float('inf'), 32),
                         '01111111100000000000000000000000',
                         "Infinity should be correctly converted to 32-bit binary")

    def test_64_bit_edge_case(self):
        self.assertEqual(convert_decimal_to_binary(float('-inf'), 64),
                         '1111111111110000000000000000000000000000000000000000000000000000',
                         "Negative infinity should be correctly converted to 64-bit binary")

if __name__ == '__main__':
    unittest.main()

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

