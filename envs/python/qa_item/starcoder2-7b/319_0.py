def count_dashes(s: str) -> int:
    return s.count('-')
import unittest


class TestCountDashes(unittest.TestCase):

    def test_no_dashes(self):
        """Should return 0 for a string with no dashes."""
        result = count_dashes('hello world')
        self.assertEqual(result, 0)  # 'hello world' contains no dashes

    def test_one_dash(self):
        """Should return 1 for a string with one dash."""
        result = count_dashes('hello-world')
        self.assertEqual(result, 1)  # 'hello-world' contains one dash

    def test_multiple_dashes(self):
        """Should return 4 for a string with multiple dashes."""
        result = count_dashes('a-b-c-d-e')
        self.assertEqual(result, 4)  # 'a-b-c-d-e' contains four dashes

    def test_dashes_at_ends(self):
        """Should return 3 for a string with dashes at the beginning and end."""
        result = count_dashes('-start-end-')
        self.assertEqual(result, 3)  # '-start-end-' contains three dashes

    def test_empty_string(self):
        """Should return 0 for an empty string."""
        result = count_dashes('')
        self.assertEqual(result, 0)  # An empty string contains no dashes

if __name__ == '__main__':
    unittest.main()