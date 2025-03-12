from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t)
    
    l, r = 0, 0
    formed = 0
    window_counts = {}
    
    ans = float("inf"), None, None
    
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        
        while l <= r and formed == required:
            character = s[l]
            
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            
            l += 1    
        
        r += 1
    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
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