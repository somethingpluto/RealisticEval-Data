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
    
    required_chars = Counter(t)
    missing_chars = len(t)
    left, right = 0, 0
    min_window_size = float('inf')
    min_window_start = 0
    
    for right, char in enumerate(s):
        if char in required_chars:
            if required_chars[char] > 0:
                missing_chars -= 1
            required_chars[char] -= 1
            
            while missing_chars == 0:
                if right - left + 1 < min_window_size:
                    min_window_size = right - left + 1
                    min_window_start = left
                
                if s[left] in required_chars:
                    required_chars[s[left]] += 1
                    if required_chars[s[left]] > 0:
                        missing_chars += 1
                
                left += 1
    
    return "" if min_window_size == float('inf') else s[min_window_start:min_window_start + min_window_size]
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