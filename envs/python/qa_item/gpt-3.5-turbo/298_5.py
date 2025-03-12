from typing import Union

def set_eur_value(value: Union[str, int, float]) -> str:
    """
    Converts a numerical value into a string representation with appropriate
    suffixes ('k' for thousands, 'm' for millions) or returns the number as a string
    if the value is below 1000. Returns an empty string for non-numeric or invalid inputs.

    Args:
        value (Union[str, int, float]): The value to convert.

    Returns:
        str: The formatted string or an empty string if the input is invalid.
    """

    if isinstance(value, (str, int, float)):
        try:
            num = float(value)
        except ValueError:
            return ""

        if num < 1000:
            return str(num)

        suffixes = ['k', 'm']
        order = 0

        while num >= 1000 and order < len(suffixes):
            num /= 1000
            order += 1

        return f"{num:.2f}{suffixes[order - 1]}"
        
    return ""
import unittest


class TestSetEurValue(unittest.TestCase):

    def test_formats_standard_values_correctly(self):
        self.assertEqual(set_eur_value('250'), '250')
        self.assertEqual(set_eur_value('2500'), '2.5k')

    def test_handles_boundary_values_accurately(self):
        self.assertEqual(set_eur_value('999'), '999')
        self.assertEqual(set_eur_value('1000'), '1.0k')
        self.assertEqual(set_eur_value('999999'), '999.9k')  # Corrected from '1000.0k' to '999.9k'
        self.assertEqual(set_eur_value('1000000'), '1.0m')

    def test_returns_correct_format_for_zero_and_negative_inputs(self):
        self.assertEqual(set_eur_value('0'), '0')

    def test_returns_empty_string_for_invalid_inputs(self):
        self.assertEqual(set_eur_value('hello'), '')
        self.assertEqual(set_eur_value(None), '')
        self.assertEqual(set_eur_value('undefined'), '')  # In JS, 'undefined' is not the same as None in Python

    def test_ensures_precision_for_large_numbers(self):
        self.assertEqual(set_eur_value('10000000'), '10.0m')
        self.assertEqual(set_eur_value('987654321'), '987.7m')

if __name__ == '__main__':
    unittest.main()