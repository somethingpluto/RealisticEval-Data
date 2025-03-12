
def simplify_windows_path(path: str) -> str:
    """
    simplify file paths in windows systems into name strings.
    For example:
        input: C:\\Users\\User\\file.txt
        output: C_Users_User_file.txt
    Args:
        path (str): windows file path str

    Returns:
        str: simplify path str
    """
    # Convert the path to lowercase
    path_lower = path.lower()

    # Remove the backslashes and forward slashes
    path = path.replace(r"\", "_")

    # Add a underscore before the last forward slash
    path = path.replace(r"\/\s+", r"\_\s+")

    return path_lower + "_" + path

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
    def test_path_with_single_backslash(self):
        self.assertEqual(simplify_windows_path(r'F:\\'), 'F_')

if __name__ == '__main__':
    unittest.main()