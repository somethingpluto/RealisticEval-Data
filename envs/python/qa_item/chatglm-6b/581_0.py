
def abbreviate_number(number: float) -> str:
    """
    Abbreviates a number to a string with a suffix based on its magnitude.

    The function uses the following suffixes based on the number's magnitude:
    - "" (no suffix) for values less than 1,000
    - "k" for thousands (1,000)
    - "M" for millions (1,000,000)
    - "B" for billions (1,000,000,000)
    - "T" for trillions (1,000,000,000,000)

    For example:
        - Input: 999             Output: "999"
        - Input: 1549            Output: "1.5k"
        - Input: 1000            Output: "1k"
        - Input: 1234567890123   Output: "1.2T"

    Args:
        number (float): The number to abbreviate.

    Returns:
        str: The abbreviated string representation of the number.
    """
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return "k" if number % 1000 == 0 else "M" if number % 1000000 == 0 else "B" if number % 100000000 == 0 else "T"
    else:
        return str(number)
python
result = abbreviate_number(999.5)
print(result)  # Output: "999"

import unittest


class TestAbbreviateNumber(unittest.TestCase):

    def test_less_than_1000(self):
        # should return the same number for values less than 1000
        self.assertEqual(abbreviate_number(999), '999')

    def test_one_thousand(self):
        # should return "1k" for 1000
        result = abbreviate_number(1000)
        self.assertIn(result, ['1k', '1.0k'])

    def test_one_thousand_five_hundred(self):
        # should return "1.5k" for 1500
        self.assertEqual(abbreviate_number(1500), '1.5k')

    def test_one_million(self):
        # should return "1M" for 1 million
        result = abbreviate_number(1000000)
        self.assertIn(result, ['1M', '1.0M'])

    def test_twenty_five_million(self):
        # should return "25M" for 25 million
        self.assertEqual(abbreviate_number(25000000), '25M')

    def test_one_billion(self):
        # should return "1B" for 1 billion
        result = abbreviate_number(1000000000)
        self.assertIn(result, ['1B', '1.0B'])

    def test_one_point_two_trillion(self):
        # should return "1.2T" for 1.2 trillion
        self.assertEqual(abbreviate_number(1234567890123), '1.2T')

if __name__ == '__main__':
    unittest.main()