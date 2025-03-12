def extract_bib_info(bib_file: str):
    """
    Extracts the title, author, and year from a BibTeX file.bib file content such as @article{sample2024,\n  author = {John Doe and Jane Smith},\n  title = {A Comprehensive Study on AI},\n  year = {2024}\n}

    Args:
        bib_file (str): The path to the BibTeX file.

    Returns:
        list of dict: A list containing dictionaries with title, author, and year for each article.
    """
    import re

    def extract_info(entry):
        title_match = re.search(r'title\s*=\s*{([^}]+)}', entry, re.IGNORECASE)
        author_match = re.search(r'author\s*=\s*{([^}]+)}', entry, re.IGNORECASE)
        year_match = re.search(r'year\s*=\s*{([^}]+)}', entry, re.IGNORECASE)
        return {
            'title': title_match.group(1).strip() if title_match else None,
            'author': author_match.group(1).strip() if author_match else None,
            'year': year_match.group(1).strip() if year_match else None
        }

    bib_data = []
    with open(bib_file, 'r') as file:
        lines = file.readlines()
        entry = ''
        for line in lines:
            if line.strip().startswith('@'):
                if entry:
                    bib_data.append(extract_info(entry))
                entry = line
            else:
                entry += line
        if entry:
            bib_data.append(extract_info(entry))
    return bib_data
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