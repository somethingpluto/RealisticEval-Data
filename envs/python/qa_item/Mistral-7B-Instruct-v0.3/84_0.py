from collections import Counter
from typing import Optional

def find_min_window_substring(source: str, target: str) -> Optional[str]:
    if not target:
        return ""

    counter_target = Counter(target)
    window_start = window_end = min_length = len(target)

    for i in range(len(source)):
        char = source[i]
        if char in counter_target:
            counter_target[char] -= 1
            if counter_target[char] >= 0:
                window_start = i

            while window_start <= window_end and all(counter_target[char] <= 0 for char in source[window_start: window_end + 1]):
                if window_end - window_start < min_length:
                    min_length = window_end - window_start + 1
                    min_window = source[window_start: window_end + 1]

                window_start += 1
                if source[window_start] in counter_target:
                    counter_target[source[window_start]] += 1

        if i == len(source) - 1:
            window_end = i

    return min_window if min_length <= len(source) else None
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