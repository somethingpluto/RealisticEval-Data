import re
from typing import Union

def clean_pattern(x: Union[str, float], pattern: str) -> Union[str, float]:
    if isinstance(x, float):
        return x
    x = str(x)
    match = re.search(pattern, x)
    if match:
        return float(match.group())
    return ""
import unittest


class TestCleanPattern(unittest.TestCase):

    def setUp(self):
        """Sets up a common regex pattern for testing."""
        self.pattern = r'(\d+\.?\d*) kg'  # Regex pattern to match weight in kg

    def test_valid_integer_weight(self):
        """Test case for valid integer weight."""
        input_string = "The weight is 25 kg"
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, 25.0)

    def test_valid_float_weight(self):
        """Test case for valid float weight."""
        input_string = "Weight measured at 15.75 kg"
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, 15.75)

    def test_no_weight_found(self):
        """Test case where no weight is present."""
        input_string = "No weight provided."
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, '')

    def test_invalid_float_conversion(self):
        """Test case for non-numeric weight."""
        input_string = "The weight is thirty kg"
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, '')

    def test_weight_with_extra_text(self):
        """Test case for weight with additional text."""
        input_string = "The total weight is 45.3 kg as per the last measurement."
        result = clean_pattern(input_string, self.pattern)
        self.assertEqual(result, 45.3)

if __name__ == '__main__':
    unittest.main()