import struct

def float_to_hex(value: float) -> str:
    """
    Converts a floating-point number to its hexadecimal representation.

    Args:
        value (float): The float value to be converted to hexadecimal.

    Returns:
        str: A string containing the hexadecimal representation of the input float.
    """
    return hex(struct.pack('f', value)[0])[2:]
import unittest

class Tester(unittest.TestCase):
    """Test case for the float_to_hex function."""

    def test_positive_float(self):
        """Test with positive float 123.456."""
        input_value = 123.456
        expected = "42f6e979"
        self.assertEqual(float_to_hex(input_value), expected)

    def test_negative_float(self):
        """Test with negative float -123.456."""
        input_value = -123.456
        expected = "c2f6e979"
        self.assertEqual(float_to_hex(input_value), expected)

    def test_zero(self):
        """Test with zero."""
        input_value = 0.0
        expected = "00000000"
        self.assertEqual(float_to_hex(input_value), expected)

    def test_small_positive_float(self):
        """Test with small positive float 0.0001."""
        input_value = 0.0001
        expected = "38d1b717"
        self.assertEqual(float_to_hex(input_value), expected)

    def test_large_float(self):
        """Test with large float 1e30."""
        input_value = 1e30
        expected = "7149f2ca"
        self.assertEqual(float_to_hex(input_value), expected)

if __name__ == '__main__':
    unittest.main()