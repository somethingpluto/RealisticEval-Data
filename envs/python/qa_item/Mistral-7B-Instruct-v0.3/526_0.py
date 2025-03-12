from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t:
        return ""

    need = Counter(t)
    window = Counter()
    start = end = ans_start = ans_end = 0

    while end < len(s):
        c = s[end]
        end += 1
        window[c] += 1

        while need - window >= 0:
            d = s[start]
            start += 1
            window[d] -= 1
            if window[d] == 0:
                del need[d]

        if not need:
            ans_start, ans_end = start, end - 1
            break

    if need:
        return ""
    return s[ans_start: ans_end + 1]
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