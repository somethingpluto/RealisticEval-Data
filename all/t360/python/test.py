import unittest


class Tester(unittest.TestCase):
    def test_get_last_part_of_filepath(self):
        # Test Case 1: Unix-style path with '/'
        self.assertEqual(get_last_part_of_filepath("/home/user/documents/file.txt"), "file.txt")

        # Test Case 2: Windows-style path with '\\'
        self.assertEqual(get_last_part_of_filepath("C:\\Users\\JohnDoe\\Documents\\file.txt"), "file.txt")

        # Test Case 3: Path without any separators (should return the original string)
        self.assertEqual(get_last_part_of_filepath("file.txt"), "file.txt")

        # Test Case 4: Path ending with a separator (should return an empty string)
        self.assertEqual(get_last_part_of_filepath("/home/user/documents/"), "")

        # Test Case 5: Path with mixed separators (should return the last part after the last separator)
        self.assertEqual(get_last_part_of_filepath("C:/Users\\JohnDoe/Documents/file.txt"), "file.txt")
