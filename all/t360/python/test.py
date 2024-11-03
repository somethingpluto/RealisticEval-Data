import unittest


class Tester(unittest.TestCase):
    def test_get_last_part_of_filepath_unix_style(self):
        self.assertEqual(get_last_part_of_filepath("/home/user/documents/file.txt"), "file.txt")

    def test_get_last_part_of_filepath_windows_style(self):
        self.assertEqual(get_last_part_of_filepath("C:\\Users\\JohnDoe\\Documents\\file.txt"), "file.txt")

    def test_get_last_part_of_filepath_no_separators(self):
        self.assertEqual(get_last_part_of_filepath("file.txt"), "file.txt")

    def test_get_last_part_of_filepath_ending_with_separator(self):
        self.assertEqual(get_last_part_of_filepath("/home/user/documents/"), "")

    def test_get_last_part_of_filepath_mixed_separators(self):
        self.assertEqual(get_last_part_of_filepath("C:/Users\\JohnDoe/Documents/file.txt"), "file.txt")
