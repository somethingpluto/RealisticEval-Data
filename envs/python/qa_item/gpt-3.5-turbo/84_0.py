from collections import Counter
from typing import Optional

def find_min_window_substring(source: str, target: str) -> Optional[str]:
    source_len = len(source)
    target_len = len(target)
    
    if source_len < target_len:
        return ""
    
    target_freq = Counter(target)
    required = len(target_freq)
    
    window_freq = {}
    formed = 0
    
    left = 0
    right = 0
    min_len = float('inf')
    result = ""
    
    while right < source_len:
        char = source[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        if char in target_freq and window_freq[char] == target_freq[char]:
            formed += 1
        
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = source[left:right+1]
            
            char = source[left]
            window_freq[char] -= 1
            
            if char in target_freq and window_freq[char] < target_freq[char]:
                formed -= 1
            
            left += 1
        
        right += 1
        
    return result
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