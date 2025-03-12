from fractions import Fraction

def convert_score_to_decimal(score_str: str) -> float:
    try:
        if '/' in score_str:
            num, denom = score_str.split('/')
            return float(Fraction(int(num), int(denom)))
        else:
            return float(score_str)
    except ValueError:
        return None
import unittest


class TestConvertScoreToDecimal(unittest.TestCase):

    def test_decimal_score(self):
        """ Test a simple decimal score. """
        self.assertEqual(convert_score_to_decimal("2.5"), 2.5)

    def test_fraction_score(self):
        """ Test a fraction score. """
        self.assertEqual(convert_score_to_decimal("10/4"), 2.5)

    def test_integer_score(self):
        """ Test an integer score represented as a string. """
        self.assertEqual(convert_score_to_decimal("5"), 5.0)

    def test_integer_divide_score(self):
        self.assertEqual(convert_score_to_decimal("12/3"), 4.0)
if __name__ == '__main__':
    unittest.main()