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
    left = 0
    right = 0
    formed_chars = 0
    window_count = {}
    ans = float("inf"), None, None

    while right < len(source):
        char = source[right]
        window_count[char] = window_count.get(char, 0) + 1
        if char in target_count and window_count[char] == target_count[char]:
            formed_chars += 1

        while left <= right and formed_chars == required_chars:
            char = source[left]

            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed_chars -= 1

            left += 1

        right += 1

    return "" if ans[0] == float("inf") else source[ans[1]:ans[2] + 1]
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