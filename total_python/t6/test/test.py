import unittest


class TestSimplifyPath(unittest.TestCase):
    def test_windows_path(self):
        self.assertEqual(simplify_path(r"D:\downloads\test.py"), "D_downloads_test.py")

    def test_linux_path(self):
        self.assertEqual(simplify_path("/home/user/test.py"), "home_user_test.py")

    def test_path_with_illegal_characters(self):
        self.assertEqual(simplify_path("/invalid<name>|file?.py"), "invalid_name_file_.py")

    def test_mixed_separator_path(self):
        self.assertEqual(simplify_path("C:/path\\to/some\directory/file.py"), "C_path_to_some_directory_file.py")

    def test_empty_path(self):
        self.assertEqual(simplify_path(""), "")
