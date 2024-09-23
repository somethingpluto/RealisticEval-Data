import unittest
from unittest.mock import patch


class TestDisplayTree(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.path.isdir')
    @patch('os.path.join')
    def test_empty_directory(self, mock_join, mock_isdir, mock_listdir):
        # Test displaying an empty directory
        mock_listdir.return_value = []
        mock_isdir.return_value = False

        with patch('builtins.print') as mock_print:
            display_tree('empty_dir')
            mock_print.assert_called_once_with("Displaying tree for: empty_dir with indent ''")

    @patch('os.listdir')
    @patch('os.path.isdir')
    @patch('os.path.join')
    def test_directory_with_files(self, mock_join, mock_isdir, mock_listdir):
        # Test a directory with only files
        mock_listdir.return_value = ['file1.txt', 'file2.txt']
        mock_isdir.side_effect = [False, False]

        with patch('builtins.print') as mock_print:
            display_tree('dir_with_files')
            mock_print.assert_any_call("Displaying tree for: dir_with_files with indent ''")
            mock_print.assert_any_call("├── file1.txt")
            mock_print.assert_any_call("└── file2.txt")

    @patch('os.listdir')
    @patch('os.path.isdir')
    @patch('os.path.join')
    def test_nested_directories(self, mock_join, mock_isdir, mock_listdir):
        # Test a directory with nested directories
        mock_listdir.side_effect = [['dir1', 'dir2'], ['file1'], []]
        mock_isdir.side_effect = [True, True, False, False]

        with patch('builtins.print') as mock_print:
            display_tree('nested_dir')
            mock_print.assert_any_call("Displaying tree for: nested_dir with indent ''")
            mock_print.assert_any_call("├── dir1")
            mock_print.assert_any_call("│   └── file1")
            mock_print.assert_any_call("└── dir2")

    @patch('os.listdir')
    @patch('os.path.isdir')
    @patch('os.path.join')
    def test_directory_with_permission_error(self, mock_join, mock_isdir, mock_listdir):
        # Test directory access with a permission error
        mock_listdir.side_effect = PermissionError("Permission denied")

        with patch('builtins.print') as mock_print:
            display_tree('restricted_dir')
            mock_print.assert_called_once_with("Permission denied.")

    @patch('os.listdir')
    @patch('os.path.isdir')
    @patch('os.path.join')
    def test_non_existent_directory(self, mock_join, mock_isdir, mock_listdir):
        # Test non-existent directory handling
        mock_listdir.side_effect = FileNotFoundError("Directory not found")

        with patch('builtins.print') as mock_print:
            display_tree('nonexistent_dir')
            mock_print.assert_called_once_with("Directory not found.")
