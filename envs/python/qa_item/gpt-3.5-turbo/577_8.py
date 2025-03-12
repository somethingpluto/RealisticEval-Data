from typing import List, Tuple, Dict, Any

def format_post_count(count: int) -> str:
    count_str = str(count).zfill(2)
    return f"{count_str} {'Post' if count == 1 else 'Posts'}"
import unittest


class TestFormatPostCount(unittest.TestCase):

    def test_return_one_post(self):
        """Should return "01 Post" for count of 1."""
        self.assertEqual(format_post_count(1), "01 Post")

    def test_return_two_posts(self):
        """Should return "02 Posts" for count of 2."""
        self.assertEqual(format_post_count(2), "02 Posts")

    def test_return_ten_posts(self):
        """Should return "10 Posts" for count of 10."""
        self.assertEqual(format_post_count(10), "10 Posts")

    def test_return_ninety_nine_posts(self):
        """Should return "99 Posts" for count of 99."""
        self.assertEqual(format_post_count(99), "99 Posts")

    def test_return_five_posts(self):
        """Should return "05 Posts" for count of 5."""
        self.assertEqual(format_post_count(5), "05 Posts")

if __name__ == '__main__':
    unittest.main()