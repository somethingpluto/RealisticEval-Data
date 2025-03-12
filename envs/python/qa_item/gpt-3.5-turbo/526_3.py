from collections import Counter

def min_window(s: str, t: str) -> str:
    left, right = 0, 0
    window_counts = Counter()
    target_counts = Counter(t)
    required = len(target_counts)
    formed = 0
    ans = float("inf"), None, None

    while right < len(s):
        character = s[right]
        window_counts[character] += 1
        if window_counts[character] == target_counts[character]:
            formed += 1

        while left <= right and formed == required:
            character = s[left]
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            window_counts[character] -= 1
            if window_counts[character] < target_counts[character]:
                formed -= 1

            left += 1

        right += 1

    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
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