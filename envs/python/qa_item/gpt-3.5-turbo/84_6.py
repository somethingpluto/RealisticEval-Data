from collections import Counter
from typing import Optional

def find_min_window_substring(source: str, target: str) -> Optional[str]:
    """
    Finds the smallest window in the source string that contains all characters of the target string.

    Args:
        source (str): The source string in which to search for the window.
        target (str): The target string containing the characters to be matched.

    Returns:
        Optional[str]: The smallest window in the source string that contains all characters of the target string.
                       Returns an empty string if no such window exists.
    """

    if not source or not target:
        return ""

    target_count = Counter(target)
    required_chars = len(target_count)
    window_start = 0
    window_end = 0
    min_length = float('inf')
    min_start = 0
    found_chars = 0
    source_count = Counter()
    
    while window_end < len(source):
        char = source[window_end]
        source_count[char] += 1
        if char in target_count and source_count[char] == target_count[char]:
            found_chars += 1
        
        while found_chars == required_chars:
            if window_end - window_start < min_length:
                min_length = window_end - window_start
                min_start = window_start
            
            char = source[window_start]
            source_count[char] -= 1
            if char in target_count and source_count[char] < target_count[char]:
                found_chars -= 1
            
            window_start += 1
        
        window_end += 1
    
    return source[min_start:min_start + min_length + 1] if min_length != float('inf') else ""
import unittest


class TestFindMinWindowSubstring(unittest.TestCase):

    def test_empty_source_string(self):
        # Test with an empty source string
        self.assertEqual(find_min_window_substring("", "abc"), "", "Should return an empty string when source is empty")

    def test_empty_target_string(self):
        # Test with an empty target string
        self.assertEqual(find_min_window_substring("abc", ""), "", "Should return an empty string when target is empty")

    def test_no_valid_window(self):
        # Test when there is no valid window
        self.assertEqual(find_min_window_substring("abcdef", "xyz"), "",
                         "Should return an empty string when no valid window exists")

    def test_exact_match_window(self):
        # Test when the entire source string is the exact match
        self.assertEqual(find_min_window_substring("abcd", "abcd"), "abcd",
                         "Should return the entire string when it is an exact match")

    def test_minimal_valid_window(self):
        # Test with a minimal valid window case
        self.assertEqual(find_min_window_substring("ADOBECODEBANC", "ABC"), "BANC",
                         "Should return 'BANC' as the smallest window containing all characters of 'ABC'")



if __name__ == '__main__':
    unittest.main()