import re

def convert(html: str) -> str:
    # Convert line breaks
    html = html.replace('<br>', '\n').replace('<br/>', '\n')

    # Convert paragraphs
    html = html.replace('<p>', '').replace('</p>', '\n\n')

    # Convert strong emphasis
    html = html.replace('<strong>', '**').replace('</strong>', '**')

    # Convert italics
    html = html.replace('<em>', '*').replace('</em>', '*')

    # Convert underlined text (not supported in Markdown)
    html = html.replace('<u>', '*').replace('</u>', '*')

    # Convert code snippets
    html = html.replace('<code>', '`').replace('</code>', '`')

    # Convert unordered lists
    html = re.sub(r'<ul>[\s\S]*?</ul>', '', html)

    # Convert ordered lists
    html = re.sub(r'<ol>[\s\S]*?</ol>', '', html)

    # Convert list items
    html = html.replace('<li>', '* ').replace('</li>', '\n')

    # Convert hyperlinks
    html = re.sub(r'<a href="(.*?)">(.*?)</a>', r'[\2](\1)', html)

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