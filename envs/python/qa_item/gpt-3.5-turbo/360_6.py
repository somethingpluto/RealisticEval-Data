import os

def get_last_part_of_filepath(file_path: str) -> str:
    """
    Extract the last part of a complete file path using a separator.

    If no separator is found, the original string is returned.

    Args:
        file_path (str): The complete file path as a string.

    Returns:
        str: The last part of the file path after the last separator, or the original string if no separator is found.
    """
    
    separator = os.path.sep
    parts = file_path.split(separator)
    
    if len(parts) > 1:
        return parts[-1]
    else:
        return file_path
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

if __name__ == '__main__':
    unittest.main()