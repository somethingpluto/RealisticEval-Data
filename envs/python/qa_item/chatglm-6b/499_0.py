
import re
from typing import Union

def clean_pattern(x: str, pattern: str) -> Union[str,float]:
    """
    Extracts a numeric value from the input string based on the given regex pattern.

    Args:
        x (str or any): The input from which to extract the value. It will be converted to a string.
        pattern (str): The regular expression pattern to use for matching.

    Returns:
        Union[str,float]: The extracted weight value if a match is found, otherwise an empty string.
    """
    # Define the regular expression pattern
    pattern = re.compile(pattern)

    # Iterate through the input string
    for i in range(len(x)):
        # Check if the current character is a digit
        match = pattern.search(x[i])
        if match:
            # If a match is found, extract the corresponding numeric value
            numeric_value = match.group(0)
            # If no match is found, return an empty string
            if i == len(x) - 1:
                return None
            # If a match is found, return the extracted value as a float
            return float(numeric_value)
    return None

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