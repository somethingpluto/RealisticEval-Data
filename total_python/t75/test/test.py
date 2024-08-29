import unittest
from unittest.mock import patch


class TestRenameFiles(unittest.TestCase):

    @patch('os.listdir')
    @patch('os.rename')
    def test_empty_directory(self, mock_rename, mock_listdir):
        mock_listdir.return_value = []
        rename_files('dummy_directory')
        mock_rename.assert_not_called()

    @patch('os.listdir')
    @patch('os.rename')
    def test_single_file(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['image001.png']
        with patch('builtins.print') as mock_print:
            rename_files('dummy_directory')
            mock_rename.assert_called_once_with('dummy_directory/image001.png', 'dummy_directory/image001.png')
            mock_print.assert_called_with("Renaming image001.png to image001.png")

    @patch('os.listdir')
    @patch('os.rename')
    def test_multiple_files_same_base(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['test001.png', 'test002.png']
        with patch('builtins.print') as mock_print:
            rename_files('dummy_directory')
            expected_calls = [
                unittest.mock.call('dummy_directory/test001.png', 'dummy_directory/test001.png'),
                unittest.mock.call('dummy_directory/test002.png', 'dummy_directory/test002.png')
            ]
            mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_multiple_files_different_bases(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['apple001.png', 'banana001.png']
        with patch('builtins.print') as mock_print:
            rename_files('dummy_directory')
            expected_calls = [
                unittest.mock.call('dummy_directory/apple001.png', 'dummy_directory/apple001.png'),
                unittest.mock.call('dummy_directory/banana001.png', 'dummy_directory/banana001.png')
            ]
            mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_complex_naming(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['image999-1.png', 'image999.png', 'image999-2.png']
        with patch('builtins.print') as mock_print:
            rename_files('dummy_directory')
            expected_calls = [
                unittest.mock.call('dummy_directory/image999-1.png', 'dummy_directory/image9991.png'),
                unittest.mock.call('dummy_directory/image999.png', 'dummy_directory/image9992.png'),
                unittest.mock.call('dummy_directory/image999-2.png', 'dummy_directory/image9993.png')
            ]
            mock_rename.assert_has_calls(expected_calls, any_order=True)
