import re

def extract_bib_info(bib_file: str):
    bib_info = []
    with open(bib_file, 'r') as file:
        content = file.read()
        entries = re.findall(r'@article{([^}]*)}', content)
        for entry in entries:
            title = re.search(r'title = {([^}]*)}', entry).group(1)
            author = re.search(r'author = {([^}]*)}', entry).group(1)
            year = re.search(r'year = {([^}]*)}', entry).group(1)
            bib_info.append({"title": title, "author": author, "year": year})
    
    return bib_info
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