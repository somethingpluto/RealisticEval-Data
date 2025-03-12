import re
from typing import List

def filter_content_with_context(
        content: str,
        keywords: List[str],
        lines_before: int = 1,
        lines_after: int = 1
) -> str:
    filtered_content = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        for keyword in keywords:
            if re.search(r'\b' + keyword + r'\b', line):
                start = max(0, i - lines_before)
                end = min(len(lines), i + lines_after + 1)
                filtered_content.extend(lines[start:end])
                break
    return '\n'.join(filtered_content)
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