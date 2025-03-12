def align_lines_left(str1: str, str2: str) -> Tuple[str, str]:
    max_len = max(len(str1), len(str2))
    str1 = str1.ljust(max_len)
    str2 = str2.ljust(max_len)
    return (str1, str2)
import unittest


class TestAlignLinesLeft(unittest.TestCase):

    def test_equal_length_strings(self):
        str1 = "Hello"
        str2 = "World"
        expected_str1 = "Hello"
        expected_str2 = "World"
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_first_string_longer(self):
        str1 = "Hello, World!"
        str2 = "Hi"
        expected_str1 = "Hello, World!"
        expected_str2 = "Hi           "  # 14 spaces after "Hi"
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_second_string_longer(self):
        str1 = "Hey"
        str2 = "Goodbye, friend!"
        expected_str1 = "Hey             "  # 15 spaces after "Hey"
        expected_str2 = "Goodbye, friend!"
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_empty_first_string(self):
        str1 = ""
        str2 = "World"
        expected_str1 = "     "  # 5 spaces
        expected_str2 = "World"
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_empty_second_string(self):
        str1 = "Hello"
        str2 = ""
        expected_str1 = "Hello"
        expected_str2 = "     "  # 5 spaces
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_both_strings_empty(self):
        str1 = ""
        str2 = ""
        expected_str1 = ""
        expected_str2 = ""
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)

    def test_strings_with_spaces(self):
        str1 = "Hello "
        str2 = "World  "
        expected_str1 = "Hello  "
        expected_str2 = "World  "
        aligned_str1, aligned_str2 = align_lines_left(str1, str2)
        self.assertEqual(aligned_str1, expected_str1)
        self.assertEqual(aligned_str2, expected_str2)
if __name__ == '__main__':
    unittest.main()