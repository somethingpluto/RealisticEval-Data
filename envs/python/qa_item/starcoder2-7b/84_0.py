from collections import Counter
from typing import Optional

def find_min_window_substring(source: str, target: str) -> Optional[str]:
    if not target or not source:
        return None

    target_counter = Counter(target)
    required = len(target_counter)

    left, right = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    while right < len(source):
        character = source[right]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in target_counter and window_counts[character] == target_counter[character]:
            formed += 1

        while left <= right and formed == required:
            character = source[left]

            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            window_counts[character] -= 1
            if character in target_counter and window_counts[character] < target_counter[character]:
                formed -= 1

            left += 1

        right += 1

    return "" if ans[0] == float("inf") else source[ans[1] : ans[2] + 1]
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