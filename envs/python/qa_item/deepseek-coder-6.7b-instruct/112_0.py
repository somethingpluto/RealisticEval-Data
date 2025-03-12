import re

def convert_html_headings_to_markdown(html: str) -> str:
    """
    Converts HTML heading tags (h1-h6) to corresponding Markdown headings.

    Args:
        html (str): The HTML string containing headings.

    Returns:
        str: The converted Markdown string.
    """
    # Regular expression to match HTML heading tags (h1-h6)
    heading_pattern = re.compile(r'<h([1-6])>(.*?)</h\1>', re.IGNORECASE)
    
    # Function to replace matched headings with Markdown equivalents
    def replace_heading(match):
        level = int(match.group(1))
        content = match.group(2)
        return '#' * level + ' ' + content
    
    # Replace all occurrences of heading tags with Markdown headings
    markdown = heading_pattern.sub(replace_heading, html)
    
    return markdown
import unittest


class TestConvertHtmlHeadingsToMarkdown(unittest.TestCase):

    def test_convert_h1_to_markdown(self):
        input_html = '<h1>This is a Heading 1</h1>'
        expected_output = '# This is a Heading 1'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h2_to_markdown(self):
        input_html = '<h2>This is a Heading 2</h2>'
        expected_output = '## This is a Heading 2'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h3_to_markdown(self):
        input_html = '<h3>This is a Heading 3</h3>'
        expected_output = '### This is a Heading 3'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h4_to_markdown(self):
        input_html = '<h4>This is a Heading 4</h4>'
        expected_output = '#### This is a Heading 4'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h5_to_markdown(self):
        input_html = '<h5>This is a Heading 5</h5>'
        expected_output = '##### This is a Heading 5'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h6_to_markdown(self):
        input_html = '<h6>This is a Heading 6</h6>'
        expected_output = '###### This is a Heading 6'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

if __name__ == '__main__':
    unittest.main()