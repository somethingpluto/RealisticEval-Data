import unittest
from unittest.mock import mock_open, patch


class TestReadMappingFile(unittest.TestCase):
    def test_invalid_format(self):
        # Test handling of a file with incorrect format (missing comma)
        file_content = "'pattern' 'replacement'"
        m_open = mock_open(read_data=file_content)
        with patch('builtins.open', m_open):
            with self.assertRaises(ValueError):
                read_mapping_file('fake_path.txt')

    def test_empty_file(self):
        # Test handling of an empty file
        m_open = mock_open(read_data="")
        with patch('builtins.open', m_open):
            result = read_mapping_file('fake_path.txt')
            self.assertEqual(result, [])

    def test_file_not_found(self):
        # Test file not found error
        with patch('builtins.open', side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_mapping_file('nonexistent_path.txt')
