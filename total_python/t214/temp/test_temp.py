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

import re


def read_mapping_file(mapping_file_path):
    """
    Read a mapping file and return a list of tuples with compiled regex and replacement strings.

    Args:
    mapping_file_path (str): Path to the file containing regex mappings.

    Returns:
    list of tuples: Each tuple contains a compiled regex object and a corresponding replacement string.

    Raises:
    FileNotFoundError: If the mapping file does not exist.
    ValueError: If any line in the file does not contain exactly one comma.

    Example of file format:
    'old_pattern1','new_word1'
    'old_pattern2','new_word2'
    """
    mappings = []
    try:
        with open(mapping_file_path, 'r') as mapping_file:
            for line in mapping_file:
                if ',' not in line:
                    raise ValueError(
                        "Each line must contain exactly one comma separating the pattern and the replacement.")

                old_pattern, new_word = line.strip().split(',', 1)
                old_pattern = old_pattern.strip().strip("'")  # Remove leading/trailing spaces and single quotes
                new_word = new_word.strip().strip("'")  # Remove leading/trailing spaces and single quotes
                mappings.append((re.compile(old_pattern), new_word))
    except FileNotFoundError:
        raise FileNotFoundError(f"Unable to find the specified file: {mapping_file_path}")

    return mappings