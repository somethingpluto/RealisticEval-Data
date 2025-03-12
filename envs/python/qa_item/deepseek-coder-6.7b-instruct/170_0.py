import re

def convert(html: str) -> str:
    """
    Converts a string containing HTML to a Markdown-formatted string.

    Args:
        html (str): The input string containing HTML content.

    Returns:
        str: A string formatted in Markdown, reflecting the input HTML structure.
    """
    # Replace line breaks
    markdown = re.sub(r'<br\s*/?>', '\n', html)
    
    # Replace paragraphs
    markdown = re.sub(r'<p>', '', markdown)
    markdown = re.sub(r'</p>', '\n\n', markdown)
    
    # Replace strong emphasis
    markdown = re.sub(r'<strong>', '**', markdown)
    markdown = re.sub(r'</strong>', '**', markdown)
    
    # Replace italics
    markdown = re.sub(r'<em>', '*', markdown)
    markdown = re.sub(r'</em>', '*', markdown)
    
    # Replace underlined text
    markdown = re.sub(r'<u>', '*', markdown)
    markdown = re.sub(r'</u>', '*', markdown)
    
    # Replace code snippets
    markdown = re.sub(r'<code>', '`', markdown)
    markdown = re.sub(r'</code>', '`', markdown)
    
    # Remove unordered lists tags
    markdown = re.sub(r'<ul>', '', markdown)
    markdown = re.sub(r'</ul>', '', markdown)
    
    # Remove ordered lists tags
    markdown = re.sub(r'<ol>', '', markdown)
    markdown = re.sub(r'</ol>', '', markdown)
    
    # Replace list items
    markdown = re.sub(r'<li>', '* ', markdown)
    markdown = re.sub(r'</li>', '\n', markdown)
    
    # Replace hyperlinks
    markdown = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r'[\2](\1)', markdown)
    
    return markdown.strip()
import unittest

class TestAnswer(unittest.TestCase):
    
    def test_simple_line_break(self):
        input_html = "Hello<br>World"
        expected_output = "Hello\nWorld"
        self.assertEqual(expected_output, convert(input_html))
    
    def test_strong_tags(self):
        input_html = "This is <strong>important</strong> text."
        expected_output = "This is **important** text."
        self.assertEqual(expected_output, convert(input_html))
    
    def test_emphasis_tags(self):
        input_html = "This is <em>emphasized</em> text."
        expected_output = "This is *emphasized* text."
        self.assertEqual(expected_output, convert(input_html))
    
    def test_unordered_list(self):
        input_html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
        expected_output = "* Item 1\n* Item 2"
        self.assertEqual(expected_output, convert(input_html))
    
    def test_anchor_tags(self):
        input_html = 'Check this link: <a href="http://example.com">Example</a>.'
        expected_output = 'Check this link: [Example](http://example.com).'
        self.assertEqual(expected_output, convert(input_html))
if __name__ == '__main__':
    unittest.main()