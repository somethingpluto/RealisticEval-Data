import struct

def hex_string_to_float(hex_str: str) -> float:
    """
    Parses a given hexadecimal string into its corresponding floating-point number and returns the float value.

    Args:
        hex_str (str): The hexadecimal string to be parsed.

    Returns:
        float: The corresponding floating-point number.
    """
    # Convert hexadecimal string to binary string
    hex_int = int(hex_str, 16)
    binary_str = bin(hex_int)[2:].zfill(64)
    
    # Convert binary string to IEEE 754 floating-point representation
    sign = int(binary_str[0])
    exponent = int(binary_str[1:12], 2) - 1023
    fraction = int(binary_str[12:], 2) / (2 ** 52) + 1
    result = (-1) ** sign * fraction * (2 ** exponent)
    
    return struct.unpack('d', struct.pack('Q', hex_int))[0]
import unittest

class Tester(unittest.TestCase):
    
    def test_positive_number(self):
        """Positive number: 40490FDB"""
        hex_str = "40490FDB"  # 3.14159 in float
        result = hex_string_to_float(hex_str)
        self.assertAlmostEqual(result, 3.14159, delta=0.00001)

    def test_negative_number(self):
        """Negative number: C0490FDB"""
        hex_str = "C0490FDB"  # -3.14159 in float
        result = hex_string_to_float(hex_str)
        self.assertAlmostEqual(result, -3.14159, delta=0.00001)

    def test_zero(self):
        """Zero: 00000000"""
        hex_str = "00000000"  # 0.0 in float
        result = hex_string_to_float(hex_str)
        self.assertAlmostEqual(result, 0.0, delta=0.00001)

    def test_small_positive_number(self):
        """Small positive number: 3F800000"""
        hex_str = "3F800000"  # 1.0 in float
        result = hex_string_to_float(hex_str)
        self.assertAlmostEqual(result, 1.0, delta=0.00001)

    def test_small_negative_number(self):
        """Small negative number: BF800000"""
        hex_str = "BF800000"  # -1.0 in float
        result = hex_string_to_float(hex_str)
        self.assertAlmostEqual(result, -1.0, delta=0.00001)


if __name__ == '__main__':
    unittest.main()