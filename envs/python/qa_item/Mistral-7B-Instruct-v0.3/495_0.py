import re
from typing import List

def filter_content_with_context(content: str, keywords: List[str], lines_before: int = 1, lines_after: int = 1) -> str:
    pattern = r'\b(' + '|'.join(keywords) + r'\b)'
    matched_lines = [(m.start(0), m.end(0)) for m in re.finditer(pattern, content, re.IGNORECASE)]

    start = 0
    end = len(content)
    filtered_content = ''

    for match in sorted(matched_lines, key=lambda x: x[0]):
        line_start = max(start - lines_before, 0)
        line_end = min(end, match[0] - lines_before)
        line_before = content[line_start: line_end].strip()

        filtered_content += line_before + '\n'
        filtered_content += content[match[0]: match[1]] + '\n'

        line_start = match[1] + lines_after
        line_end = min(end, line_start)
        line_after = content[line_start: line_end].strip()

        filtered_content += line_after + '\n'

    return filtered_content.strip()
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