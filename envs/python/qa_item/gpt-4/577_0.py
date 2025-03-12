def format_post_count(count: int) -> str:
    """
    Formats the post count into a human-readable string.

    The function formats the number of posts into a two-digit string
    followed by "Post" or "Posts" based on the count.

    For example:
        - Input: 3  Output: "02 Posts"
        - Input: 1  Output: "01 Post"

    Args:
        count (int): The number of posts.

    Returns:
        str: A formatted string indicating the number of posts.
             The string will be in the format "XX Post" or "XX Posts",
             where XX is the count formatted as a two-digit number.
    """
    formatted_count = str(count).zfill(2)  # Zero-fill the count to ensure it's two digits
    if count == 1:
        return f"{formatted_count} Post"
    else:
        return f"{formatted_count} Posts"
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