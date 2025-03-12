from typing import List

def abbreviate_number(number: float) -> str:
    suffixes = ["", "k", "M", "B", "T"]
    magnitude = 0
    
    while number >= 1000 and magnitude < len(suffixes)-1:
        number /= 1000
        magnitude += 1
        
    return f"{number:.1f}{suffixes[magnitude]}"
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