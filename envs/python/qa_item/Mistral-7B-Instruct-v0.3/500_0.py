import re

def convert_score_to_decimal(score_str: str) -> float:
    """
    Converts the string representation of a score to its decimal value.
    For example:
        input: 10/4
        output: 2.5
    Args:
        score_str (str): The score as a string, can be a decimal or a fraction

    Returns:
        float: The decimal value of the score as a float, or None if the input is invalid
    """
    # Check if the score is a decimal or a fraction
    match = re.match(r'^(-?\d+(\.\d+)?)($|/(-?\d+))?$', score_str)

    if match:
        # If it's a decimal, return the float value
        if not match.group(3):
            return float(match.group(1))
        # If it's a fraction, calculate the decimal value
        numerator = int(match.group(1))
        denominator = int(match.group(4))
        return float(numerator) / float(denominator)
    else:
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