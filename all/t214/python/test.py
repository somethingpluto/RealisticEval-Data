import unittest
from unittest.mock import mock_open, patch


class TestReadMappingFile(unittest.TestCase):
    def test_valid_mappings(self):
        # Setup a mock file with valid content
        file_content = "'^abc$','xyz'\n'^def$','uvw'"
        m_open = mock_open(read_data=file_content)
        with patch('builtins.open', m_open):
            result = read_mapping_file('fake_path.txt')
            # Verify that the function reads the file and processes the content correctly
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0][0].pattern, '^abc$')
            self.assertEqual(result[0][1], 'xyz')
            self.assertEqual(result[1][0].pattern, '^def$')
            self.assertEqual(result[1][1], 'uvw')

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

    def test_comma_in_replacement(self):
        # Test handling of a comma within the replacement string
        file_content = "'^abc$','xy,z'"
        m_open = mock_open(read_data=file_content)
        with patch('builtins.open', m_open):
            result = read_mapping_file('fake_path.txt')
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0][0].pattern, '^abc$')
            self.assertEqual(result[0][1], 'xy,z')
