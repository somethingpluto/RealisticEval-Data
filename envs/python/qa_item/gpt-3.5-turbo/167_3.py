import re

def assert999(bit_name: str) -> bool:
    if not bit_name.endswith(".bit"):
        return False
    
    num_str = bit_name[:-4]  # Remove ".bit" suffix
    if not num_str.isdigit():
        return False
    
    num = int(num_str)
    if num < 0 or num > 999:
        return False
    
    return True
import unittest


class TestAssert999(unittest.TestCase):
    def test_valid_three_digit_number_with_suffix(self):
        """Test case for a valid 3-digit number with the ".bit" suffix. Expected to return true."""
        input_value = "123.bit"
        result = assert999(input_value)
        self.assertTrue(result)

    def test_valid_two_digit_number_with_suffix(self):
        """Test case for a valid 2-digit number with the ".bit" suffix. Expected to return true."""
        input_value = "12.bit"
        result = assert999(input_value)
        self.assertTrue(result)

    def test_non_numeric_characters_after_suffix(self):
        """Test case for a string containing non-numeric characters after removing ".bit". Expected to return false."""
        input_value = "12a.bit"
        result = assert999(input_value)
        self.assertFalse(result)

    def test_lower_boundary_value(self):
        """Test case for the lower boundary value "0.bit". Expected to return true."""
        input_value = "0.bit"
        result = assert999(input_value)
        self.assertTrue(result)

    def test_upper_boundary_value(self):
        """Test case for the upper boundary value "999.bit". Expected to return true."""
        input_value = "999.bit"
        result = assert999(input_value)
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()