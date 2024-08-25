import unittest

class TestSimplifyWindowsPath(unittest.TestCase):
    def test_simple_path(self):
        self.assertEqual(simplify_windows_path("C:\\Users\\User\\file.txt"), "C_Users_User_file.txt")

    def test_path_with_spaces(self):
        self.assertEqual(simplify_windows_path("E:\\New Folder\\my file.docx"), "E_New Folder_my file.docx")

    def test_path_with_drive_only(self):
        self.assertEqual(simplify_windows_path("F:\\"), "F_")

    def test_path_with_special_characters(self):
        self.assertEqual(simplify_windows_path("D:\\data\\new-year@2020\\report#1.pdf"), "D_data_new-year@2020_report#1.pdf")

    def test_nested_directories(self):
        self.assertEqual(simplify_windows_path("G:\\folder1\\folder2\\folder3\\file.jpeg"), "G_folder1_folder2_folder3_file.jpeg")
import os


def simplify_windows_path(path):
    # Replace the drive letter and colon, e.g., 'D:' with 'D_'
    drive, path_without_drive = os.path.splitdrive(path)
    simplified_drive = drive.rstrip(':') + '_'

    # Replace backslashes with underscores and strip any trailing backslash
    simplified_path = path_without_drive.replace('\\', '_').strip('_')

    # Concatenate the simplified drive and the remaining path
    final_path = simplified_drive + simplified_path

    return final_path
