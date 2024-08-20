import os
import unittest
from unittest.mock import patch


class TestRenameFiles(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.rename')
    def test_typical_files(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['image001.png', 'image002.png', 'image003.png']
        directory = '/fake/directory'
        rename_files(directory)
        calls = [patch.call(os.path.join(directory, 'image001.png'), os.path.join(directory, 'image001.png')),
                 patch.call(os.path.join(directory, 'image002.png'), os.path.join(directory, 'image002.png')),
                 patch.call(os.path.join(directory, 'image003.png'), os.path.join(directory, 'image003.png'))]
        mock_rename.assert_has_calls(calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_empty_directory(self, mock_rename, mock_listdir):
        mock_listdir.return_value = []
        directory = '/fake/directory'
        rename_files(directory)
        mock_rename.assert_not_called()

    @patch('os.listdir')
    @patch('os.rename')
    def test_complex_file_names(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['data100-1.png', 'data100-2.png', 'info100-1.png']
        directory = '/fake/directory'
        rename_files(directory)
        expected_calls = [patch.call(os.path.join(directory, 'data100-1.png'), os.path.join(directory, 'data001.png')),
                          patch.call(os.path.join(directory, 'data100-2.png'), os.path.join(directory, 'data002.png')),
                          patch.call(os.path.join(directory, 'info100-1.png'), os.path.join(directory, 'info001.png'))]
        mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_mixed_case_sensitivity(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['Image001.PNG', 'image002.png', 'IMAGE003.Png']
        directory = '/fake/directory'
        rename_files(directory)
        expected_calls = [patch.call(os.path.join(directory, 'Image001.PNG'), os.path.join(directory, 'Image001.png')),
                          patch.call(os.path.join(directory, 'image002.png'), os.path.join(directory, 'image002.png')),
                          patch.call(os.path.join(directory, 'IMAGE003.Png'), os.path.join(directory, 'IMAGE003.png'))]
        mock_rename.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('os.rename')
    def test_sequential_renaming_reset(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['set101.png', 'set102.png', 'newset101.png']
        directory = '/fake/directory'
        rename_files(directory)
        expected_calls = [patch.call(os.path.join(directory, 'set101.png'), os.path.join(directory, 'set001.png')),
                          patch.call(os.path.join(directory, 'set102.png'), os.path.join(directory, 'set002.png')),
                          patch.call(os.path.join(directory, 'newset101.png'), os.path.join(directory, 'newset001.png'))]
        mock_rename.assert_has_calls(expected_calls, any_order=True)