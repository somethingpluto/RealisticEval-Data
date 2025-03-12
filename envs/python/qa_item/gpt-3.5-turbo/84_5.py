from collections import Counter
from typing import Optional

def find_min_window_substring(source: str, target: str) -> Optional[str]:
    source_len = len(source)
    target_len = len(target)
    
    if source_len < target_len:
        return ""
    
    target_counter = Counter(target)
    window_counter = Counter()
    
    min_len = float('inf')
    min_start = 0
    min_end = 0
    
    required_chars = len(target_counter)
    chars_found = 0
    
    start = 0
    end = 0
    
    while end < source_len:
        char_end = source[end]
        window_counter[char_end] += 1
        
        if window_counter[char_end] == target_counter[char_end]:
            chars_found += 1
        
        while chars_found == required_chars and start <= end:
            char_start = source[start]
            current_len = end - start + 1
            
            if current_len < min_len:
                min_len = current_len
                min_start = start
                min_end = end
            
            window_counter[char_start] -= 1
            if char_start in target_counter and window_counter[char_start] < target_counter[char_start]:
                chars_found -= 1
            
            start += 1
        
        end += 1
    
    if min_len == float('inf'):
        return ""
    
    return source[min_start:min_end + 1]
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