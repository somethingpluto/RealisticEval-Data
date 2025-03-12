
def get_last_part_of_filepath(file_path: str) -> str:
    """
    Extract the last part of a complete file path using a separator.

    If no separator is found, the original string is returned.

    Args:
        file_path (str): The complete file path as a string.

    Returns:
        str: The last part of the file path after the last separator, or the original string if no separator is found.
    """
    if file_path.endswith(".txt"):
        last_part = file_path[:-4] + ".txt"
    elif file_path.endswith(".csv"):
        last_part = file_path[:-6] + ".csv"
    else:
        last_part = file_path
    return last_part

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

if __name__ == '__main__':
    unittest.main()