import unittest
from unittest.mock import patch, mock_open


class TestFileUtilityFunctions(unittest.TestCase):

    def test_read_file_should_return_file_content_as_string(self):
        mock_content = 'Hello, world!'
        with patch('builtins.open', mock_open(read_data=mock_content)):
            result = read_file('/path/to/file.txt')
            self.assertEqual(result, mock_content)

    def test_read_file_should_return_empty_string_for_empty_file(self):
        mock_content = ''
        with patch('builtins.open', mock_open(read_data=mock_content)):
            result = read_file('/path/to/emptyfile.txt')
            self.assertEqual(result, mock_content)

    def test_read_file_should_throw_error_if_file_cannot_be_read(self):
        with patch('builtins.open', side_effect=FileNotFoundError('File not found')):
            with self.assertRaises(OSError) as context:
                read_file('/invalid/path.txt')
            self.assertEqual(str(context.exception), 'Unable to read file at /invalid/path.txt: File not found')

    def test_write_file_should_throw_error_if_file_cannot_be_written(self):
        with patch('builtins.open', side_effect=PermissionError('Permission denied')):
            with self.assertRaises(OSError) as context:
                write_file('/invalid/path.txt', 'data')
            self.assertEqual(str(context.exception), 'Unable to write file at /invalid/path.txt: Permission denied')

    def test_read_file_should_handle_large_files_correctly(self):
        mock_content = 'a' * 10000  # 10,000 characters long string
        with patch('builtins.open', mock_open(read_data=mock_content)):
            result = read_file('/path/to/largefile.txt')
            self.assertEqual(result, mock_content)