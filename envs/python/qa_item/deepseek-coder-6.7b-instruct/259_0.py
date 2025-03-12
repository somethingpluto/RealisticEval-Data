def is_compliant_four_digit(number: int) -> bool:
    """
    Determine whether a number is a compliant four-digit number.

    Args:
        number (int): The number to check.

    Returns:
        True if the number is a compliant four-digit number, False otherwise.
    """
    # Check if the number is a four-digit number
    if 1000 <= number <= 9999:
        # Check if the number has at least two different digits
        digits = set(str(number))
        return len(digits) >= 2
    return False
import unittest


class TestIsCompliantFourDigit(unittest.TestCase):
    def test_positive_four_digit_number(self):
        # Tests a standard positive four-digit number
        self.assertTrue(is_compliant_four_digit(1234))

    def test_boundary_values(self):
        # Tests the boundary values of the range
        self.assertTrue(is_compliant_four_digit(1000))
        self.assertTrue(is_compliant_four_digit(9999))

    def test_negative_four_digit_number(self):
        # Tests a negative four-digit number
        self.assertFalse(is_compliant_four_digit(-1234))

    def test_out_of_range_number(self):
        # Tests numbers that are out of the four-digit range
        self.assertFalse(is_compliant_four_digit(999))
        self.assertFalse(is_compliant_four_digit(10000))
if __name__ == '__main__':
    unittest.main()