import re

def hex_string_to_float(hex_str: str) -> float:
    """
    Parses a given hexadecimal string into its corresponding floating-point number and returns the float value.

    Args:
        hex_str (str): The hexadecimal string to be parsed.

    Returns:
        float: The corresponding floating-point number.
    """
    # Ensure the input is a valid hexadecimal string
    if not re.match(r'^0x[0-9a-fA-F]*\.?[0-9a-fA-F]*$', hex_str):
        raise ValueError("Invalid hexadecimal string")

    # Split the hexadecimal string into parts: sign, integer, and fraction
    sign, integer, fraction = hex_str[0], hex_str[1:len(hex_str) - len(fraction)], fraction

    # Convert the integer and fraction parts to integers
    int_part = int(integer, 16)
    frac_part = 0
    if fraction:
        frac_part = int(fraction, 16) / (16 ** len(fraction))

    # Add the sign if it exists
    if sign == '-':
        int_part = -int_part

    # Return the final float value
    return int_part + frac_part
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