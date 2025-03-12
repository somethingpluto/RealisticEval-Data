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

    target_counts = Counter(target)
    required_chars = len(target_counts)
    window_start = 0
    window_end = 0
    min_window_size = float('inf')
    min_window_start = 0
    found_chars = 0
    source_counts = Counter()

    while window_end < len(source):
        char_end = source[window_end]
        source_counts[char_end] += 1

        if char_end in target_counts and source_counts[char_end] == target_counts[char_end]:
            found_chars += 1

        while found_chars == required_chars:
            current_window_size = window_end - window_start + 1
            if current_window_size < min_window_size:
                min_window_size = current_window_size
                min_window_start = window_start

            char_start = source[window_start]
            source_counts[char_start] -= 1

            if char_start in target_counts and source_counts[char_start] < target_counts[char_start]:
                found_chars -= 1

            window_start += 1

        window_end += 1

    if min_window_size == float('inf'):
        return ""
    
    return source[min_window_start:min_window_start + min_window_size]
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