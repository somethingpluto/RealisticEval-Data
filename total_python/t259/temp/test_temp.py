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

    def test_non_integer_input(self):
        # Tests inputs that are not integers (string, float)
        self.assertFalse(is_compliant_four_digit('1234'))
        self.assertFalse(is_compliant_four_digit(1234.0))

    def test_out_of_range_number(self):
        # Tests numbers that are out of the four-digit range
        self.assertFalse(is_compliant_four_digit(999))
        self.assertFalse(is_compliant_four_digit(10000))
def is_compliant_four_digit(number):
    """
    Determines whether the given number is a compliant four-digit number.
    Compliance is defined as the number being between 1000 and 9999, inclusive.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if the number is a compliant four-digit number, False otherwise.
    """
    if not isinstance(number, int):
        return False  # Ensures the function only processes integers

    # Check if the number is strictly between 1000 and 9999
    return 1000 <= number <= 9999