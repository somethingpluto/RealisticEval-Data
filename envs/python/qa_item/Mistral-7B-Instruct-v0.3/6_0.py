import os
import re

def simplify_windows_path(path: str) -> str:
    """
    Simplify file paths in Windows systems into name strings.
    For example:
        input: C:\\Users\\User\\file.txt
        output: C_Users_User_file.txt
    Args:
        path (str): windows file path str

    Returns:
        str: simplify path str
    """
    # Replace backslashes with underscores
    path = path.replace('\\', '_')

    # Replace colons with underscores
    path = re.sub(r'^[A-Z]:', r'_\g<0>', path)

    # Replace spaces with underscores
    path = path.replace(' ', '_')

    # Replace periods with underscores in file names
    path = re.sub(r'\.[a-zA-Z]+$', r'_file\g<0>', path)

    return path
import unittest


class TestSimplifyWindowsPath(unittest.TestCase):
    def test_simple_path(self):
        self.assertEqual(simplify_windows_path(r"C:\Users\User\file.txt"), "C_Users_User_file.txt")

    def test_simple_path2(self):
        self.assertEqual(simplify_windows_path(r"D:\User\file.txt"), "D_User_file.txt")

    def test_path_with_spaces(self):
        self.assertEqual(simplify_windows_path(r"E:\New Folder\my file.docx"), "E_New Folder_my file.docx")

    def test_nested_directories(self):
        self.assertEqual(simplify_windows_path(r"G:\folder1\folder2\folder3\file.jpeg"),
                         "G_folder1_folder2_folder3_file.jpeg")

if __name__ == '__main__':
    unittest.main()