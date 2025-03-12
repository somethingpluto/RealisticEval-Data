import re
from urllib.parse import urlparse

def convert(html: str) -> str:
    """
    Converts a string containing HTML to a Markdown-formatted string.
    """

    # Line breaks, paragraphs, strong emphasis, italics, underlined text, code snippets
    markdown_map = {
        ('<br>', '</br>', '\n'),
        ('<p>', '</p>', '\n\n'),
        ('<strong>', '</strong>', '**'),
        ('<em>', '</em>', '*'),
        ('<u>', '</u>', '*'),
        ('<code>', '</code>', '`'),
    }

    # List items
    list_map = {
        ('<li>', '</li>', '*\n'),
    }

    # Hyperlinks
    link_map = {
        ('<a href="', '">', '[']
    }

    # Replace all occurrences of the specified HTML tags with their Markdown equivalents
    for from_tag, to_tag, replacement in markdown_map + list_map + [link_map]:
        html = html.replace(*from_tag, *to_tag).replace(from_tag[0], replacement)

    # Extract hyperlink text and URL
    def extract_link_text_and_url(match):
        link_text, link_url = match.groups()
        return link_text, link_url.strip('"')

    # Replace hyperlinks with Markdown format
    link_pattern = re.compile(r'<a\s+href="(.*?)"\s*>(.*?)</a>')
    for link_text, link_url in map(extract_link_text_and_url, link_pattern.findall(html)):
        html = html.replace(link_text, f'{link_text}[{link_text}]({link_url})')

    return html
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