import re
from typing import List


def filter_content_with_context(
        content: str,
        keywords: List[str],
        lines_before: int = 1,
        lines_after: int = 1
) -> str:
    """
    Filters website content to include lines containing any of the specified keywords as whole words,
    along with a specified number of lines before and after for context. This version uses regular expressions
    to ensure exact, whole word matching and respects case sensitivity.

    Args:
        content (str): The full text content of the website.
        keywords (List[str]): A list of strings to search for within the content.
        lines_before (int): Number of lines to include before a matching line.
        lines_after (int): Number of lines to include after a matching line.

    Returns:
        str: A string containing the filtered content with additional context.
    """  

    keyword_pattern = '|'.join(r"\b{}\b".format(re.escape(keyword)) for keyword in keywords)
    pattern = re.compile(r'((.*\n){0,%d})((.*\b(?:%s)\b.*)\n){1}((.*\n){0,%d})' % (lines_before, keyword_pattern, lines_after), re.M)
    
    filtered_content = ''
    
    matches = pattern.finditer(content)
    for match in matches:
        filtered_content += match.group()
    
    return filtered_content
import unittest


class TestFilterContentWithContext(unittest.TestCase):

    def test_single_keyword_match(self):
        """Test a single keyword match with context lines."""
        content = """Line one.
        This line contains a keyword.
        Line three."""
        keywords = ["keyword"]
        expected_output = """Line one.
        This line contains a keyword.
        Line three."""
        result = filter_content_with_context(content, keywords, lines_before=1, lines_after=1)
        self.assertEqual(result.strip(), expected_output.strip(), "Failed to filter content for a single keyword.")


    def test_no_keyword_match(self):
        """Test when no keywords match."""
        content = """Line one.
        Line two.
        Line three."""
        keywords = ["missing"]
        expected_output = ""
        result = filter_content_with_context(content, keywords, lines_before=1, lines_after=1)
        self.assertEqual(result.strip(), expected_output, "Failed to return empty string for no matches.")


    def test_lines_before_and_after(self):
        """Test functionality with specified lines before and after."""
        content = """Line one.
        This line contains a keyword.
        Line three.
        Line four.
        Line five."""
        keywords = ["keyword"]
        expected_output = """Line one.
        This line contains a keyword.
        Line three."""
        result = filter_content_with_context(content, keywords, lines_before=1, lines_after=1)
        self.assertEqual(result.strip(), expected_output.strip(), "Failed to correctly include context lines.")

if __name__ == '__main__':
    unittest.main()