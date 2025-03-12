from collections import Counter

def min_window(s: str, t: str) -> str:
    """
    Find the minimum window substring in `s` that contains all characters of `t`.

    Args:
        s (str): The input string in which to search for the substring.
        t (str): The target string whose characters must be included in the substring.

    Returns:
        str: The minimum window substring of `s` that contains all characters of `t`. Returns an empty string if no such substring exists.
    """
    if not s or not t:
        return ""

    # Dictionary to store the frequency of characters in t
    t_count = Counter(t)
    required = len(t_count)

    # Dictionary to store the frequency of characters in the current window
    window_count = {}
    formed = 0

    # Pointers to represent the current window
    left, right = 0, 0

    # Variables to store the minimum window length and the start and end indices of that window
    min_length = float('inf')
    min_window_start = 0

    while right < len(s):
        # Add the current character to the window
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        # Check if the current character completes a required character count
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        # Try to contract the window until it ceases to be 'desirable'
        while left <= right and formed == required:
            char = s[left]

            # Save the smallest window until now
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window_start = left

            # The character at the position pointed by the `left` pointer is no longer a part of the window
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window
            left += 1

        # Keep expanding the window once we are done contracting
        right += 1

    # Return the minimum window substring
    return "" if min_length == float('inf') else s[min_window_start:min_window_start + min_length]
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