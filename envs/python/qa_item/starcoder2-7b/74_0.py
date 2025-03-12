import struct
from typing import Union

def convert_decimal_to_binary(decimal_value: float, bit_length: int) -> Union[str, None]:
    if bit_length not in [32, 64]:
        return None

    if bit_length == 32:
        format_char = 'f'
    else:
        format_char = 'd'

    binary_string = bin(struct.unpack('{}{}'.format(format_char, 's'), struct.pack('{}{}'.format(format_char, 's'), decimal_value))[0])[2:]

    return binary_string.zfill(bit_length)
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