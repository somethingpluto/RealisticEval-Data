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
