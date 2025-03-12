import os

def simplify_windows_path(path: str) -> str:
    simple_path = path.replace("\\", "_")
    simple_path = simple_path.replace(":", "")
    
    return simple_path
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