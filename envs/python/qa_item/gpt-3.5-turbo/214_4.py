from typing import List
import re

def read_mapping_file(mapping_file_path: str) -> List:
    regex_mappings = []
    
    with open(mapping_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                pattern, replacement = line.split(',')
                regex_mappings.append((re.compile(pattern), replacement))
    
    return regex_mappings
import re
import unittest
from unittest.mock import patch, mock_open


class TestReadMappingFile(unittest.TestCase):

    def test_valid_mapping_file(self):
        # Test with a valid mapping file content
        mock_file_content = "'old_pattern1','new_word1'\n'old_pattern2','new_word2'\n"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = read_mapping_file("dummy_path.txt")
            expected = [
                (re.compile("old_pattern1"), "new_word1"),
                (re.compile("old_pattern2"), "new_word2"),
            ]
            self.assertEqual(result, expected)

    def test_missing_file(self):
        # Test with a missing file
        with self.assertRaises(FileNotFoundError):
            read_mapping_file("non_existent_file.txt")

    def test_malformed_line_no_comma(self):
        # Test with a line that does not contain a comma
        mock_file_content = "'old_pattern1' 'new_word1'\n"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            with self.assertRaises(ValueError) as context:
                read_mapping_file("dummy_path.txt")
            self.assertEqual(str(context.exception), "Each line must contain exactly one comma separating the pattern and the replacement.")

    def test_valid_patterns_with_special_characters(self):
        # Test with valid patterns that contain special regex characters
        mock_file_content = "'\\d+', 'number'\n'\\w+', 'word'\n"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = read_mapping_file("dummy_path.txt")
            expected = [
                (re.compile(r"\d+"), "number"),
                (re.compile(r"\w+"), "word"),
            ]
            self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()