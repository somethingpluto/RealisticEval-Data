import re

def extract_bib_info(bib_file: str) -> list:
    """
    Extracts the title, author, and year from a BibTeX file.

    Args:
        bib_file (str): The path to the BibTeX file.

    Returns:
        list of dict: A list containing dictionaries with title, author, and year for each article.
    """
    with open(bib_file, 'r') as file:
        content = file.read()

    # Regular expression to match BibTeX entries
    bib_pattern = re.compile(r'@[a-zA-Z]+\{([^,]+),\s*(.*?)\}', re.DOTALL)
    entries = bib_pattern.findall(content)

    result = []

    for entry in entries:
        key, fields = entry
        field_pattern = re.compile(r'\s*([a-zA-Z]+)\s*=\s*{(.*?)}', re.DOTALL)
        fields_dict = {key: value.strip() for key, value in field_pattern.findall(fields)}

        if 'title' in fields_dict and 'author' in fields_dict and 'year' in fields_dict:
            result.append({
                'title': fields_dict['title'],
                'author': fields_dict['author'],
                'year': fields_dict['year']
            })

    return result
import re
import unittest
from unittest.mock import mock_open, patch


class TestExtractBibInfo(unittest.TestCase):

    def test_valid_entry(self):
        """Test extraction from a valid BibTeX entry."""
        mock_bib = "@article{sample2024,\n  author = {John Doe and Jane Smith},\n  title = {A Comprehensive Study on AI},\n  year = {2024}\n}"
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = [{'title': 'A Comprehensive Study on AI', 'author': 'John Doe and Jane Smith', 'year': '2024'}]
            self.assertEqual(result, expected)

    def test_multiple_entries(self):
        """Test extraction from multiple BibTeX entries."""
        mock_bib = (
            "@article{sample2024,\n"
            "  author = {John Doe},\n"
            "  title = {A Comprehensive Study on AI},\n"
            "  year = {2024}\n}\n"
            "@article{sample2023,\n"
            "  author = {Jane Smith},\n"
            "  title = {Deep Learning Techniques},\n"
            "  year = {2023}\n}"
        )
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = [
                {'title': 'A Comprehensive Study on AI', 'author': 'John Doe', 'year': '2024'},
                {'title': 'Deep Learning Techniques', 'author': 'Jane Smith', 'year': '2023'}
            ]
            self.assertEqual(result, expected)

    def test_missing_fields(self):
        """Test extraction when some fields are missing."""
        mock_bib = "@article{sample2024,\n  author = {John Doe},\n  title = {Title Missing Year}\n}"
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = [{'title': 'Title Missing Year', 'author': 'John Doe', 'year': None}]
            self.assertEqual(result, expected)

    def test_empty_file(self):
        """Test extraction from an empty BibTeX file."""
        mock_bib = ""
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = []
            self.assertEqual(result, expected)

    def test_incorrect_format(self):
        """Test extraction from a badly formatted BibTeX entry."""
        mock_bib = "@article{sample2024,\n  author = John Doe,\n  title = {Title Without Braces},\n  year = 2024\n}"
        with patch("builtins.open", mock_open(read_data=mock_bib)):
            result = extract_bib_info("dummy.bib")
            expected = [{'title': 'Title Without Braces', 'author': None, 'year': None}]
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()