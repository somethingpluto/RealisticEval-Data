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
    
    target_freq = Counter(t)
    required = len(target_freq)
    formed = 0
    left, right = 0, 0
    window_counts = {}
    
    min_len, min_idx = float('inf'), (0, 0)
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in target_freq and window_counts[char] == target_freq[char]:
            formed += 1
        
        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_idx = (left, right)
            
            window_counts[char] -= 1
            if char in target_freq and window_counts[char] < target_freq[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if min_len == float('inf') else s[min_idx[0]:min_idx[1] + 1]
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