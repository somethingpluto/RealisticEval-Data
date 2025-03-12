def is_compliant_four_digit(number: int) -> bool:
    if number >= 1000 and number <= 9999:
        return True
    else:
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