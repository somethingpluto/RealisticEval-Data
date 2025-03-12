from collections import Counter
from typing import Optional

def find_min_window_substring(source: str, target: str) -> Optional[str]:
    target_counter = Counter(target)
    required_chars = len(target_counter)
    window_counter = Counter()
    formed = 0
    left, right = 0, 0
    min_length = float('inf')
    min_window = ""

    while right < len(source):
        char = source[right]
        window_counter[char] += 1

        if char in target_counter and window_counter[char] == target_counter[char]:
            formed += 1

        while left <= right and formed == required_chars:
            char = source[left]

            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = source[left:right + 1]

            window_counter[char] -= 1
            if char in target_counter and window_counter[char] < target_counter[char]:
                formed -= 1

            left += 1

        right += 1

    return min_window if min_length != float('inf') else ""
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