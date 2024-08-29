import unittest
from unittest.mock import patch


class TestRenameFiles(unittest.TestCase):

    @patch('os.walk')
    @patch('os.rename')
    def test_no_files_present(self, mock_rename, mock_walk):
        mock_walk.return_value = [('/some/path', (), ())]
        rename_files('/some/path')
        mock_rename.assert_not_called()

    @patch('os.walk')
    @patch('os.rename')
    def test_basic_renaming(self, mock_rename, mock_walk):
        mock_walk.return_value = [('/some/path', (), ('file:1.txt',))]
        rename_files('/some/path')
        mock_rename.assert_called_once_with('/some/path/file:1.txt', '/some/path/file-1.txt')

    @patch('os.walk')
    @patch('os.rename')
    def test_no_colon_in_filenames(self, mock_rename, mock_walk):
        mock_walk.return_value = [('/some/path', (), ('file1.txt',))]
        rename_files('/some/path')
        mock_rename.assert_not_called()

    @patch('os.walk')
    @patch('os.rename')
    def test_nested_directories(self, mock_rename, mock_walk):
        mock_walk.return_value = [
            ('/some/path', ('subdir',), ('file:1.txt',)),
            ('/some/path/subdir', (), ('file:2.txt',))
        ]
        rename_files('/some/path')
        expected_calls = [
            unittest.mock.call('/some/path/file:1.txt', '/some/path/file-1.txt'),
            unittest.mock.call('/some/path/subdir/file:2.txt', '/some/path/subdir/file-2.txt')
        ]
        mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.walk')
    @patch('os.rename')
    def test_rename_failure(self, mock_rename, mock_walk):
        mock_walk.return_value = [('/some/path', (), ('file:1.txt',))]
        mock_rename.side_effect = OSError('Permission denied')
        with self.assertLogs(level='ERROR') as log:
            rename_files('/some/path')
            self.assertIn('Error renaming', log.output[0])