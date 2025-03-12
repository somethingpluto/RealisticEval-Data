
from collections import Counter

def min_window(s: str, t: str) -> str:
    """
    Find the minimum window substring in `s` that contains all characters of `t`.

    Args:
        s (str): The input string in which to search for the substring.
        t (str): The target string whose characters must be included in the substring.

    Returns:
        str: The minimum window substring of `s` that contains all characters of `t`.Returns an empty string if no such substring exists.
    """
    # Create a Counter object to store the characters of t
    char_ Counter = Counter(t.split())

    # Initialize the result to an empty string
    result = ""

    # Loop through each character in s
    for char in s:
        # Check if the current character is in t
        if char in char_ Counter:
            # If it is, find the minimum window substring starting from the current character
            min_window_substring = result + char_ Counter[char][0]
            # If it exists, return it
            if min_window_substring:
                return min_window_substring
        # If not, add the current character to the result
        result += char

    # If no such substring exists, return an empty string
    return result

import unittest


class TestMinWindow(unittest.TestCase):

    def test_basic_case(self):
        """Test with a normal case where the minimum window exists."""
        s = "ADOBECODEBANC"
        t = "ABC"
        expected_output = "BANC"
        self.assertEqual(min_window(s, t), expected_output)

    def test_no_window_exists(self):
        """Test where no window can satisfy the condition."""
        s = "A"
        t = "AA"
        expected_output = ""
        self.assertEqual(min_window(s, t), expected_output)

    def test_empty_string(self):
        """Test with an empty input string s."""
        s = ""
        t = "ABC"
        expected_output = ""
        self.assertEqual(min_window(s, t), expected_output)


    def test_multiple_valid_windows(self):
        """Test with multiple valid windows to ensure the smallest one is returned."""
        s = "AA"
        t = "AA"
        expected_output = "AA"
        self.assertEqual(min_window(s, t), expected_output)

if __name__ == '__main__':
    unittest.main()