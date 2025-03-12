import re

def convert(html: str) -> str:
    html = html.replace('<br>', '\n').replace('<br/>', '\n')
    html = re.sub(r'<p>', '', html)
    html = re.sub(r'</p>', '\n\n', html)
    html = html.replace('<strong>', '**').replace('</strong>', '**')
    html = html.replace('<em>', '*').replace('</em>', '*')
    html = html.replace('<u>', '*').replace('</u>', '*')
    html = html.replace('<code>', '`').replace('</code>', '`')
    html = re.sub(r'<ul>', '', html)
    html = re.sub(r'</ul>', '', html)
    html = re.sub(r'<ol>', '', html)
    html = re.sub(r'</ol>', '', html)
    html = re.sub(r'<li>', '* ', html)
    html = re.sub(r'</li>', '\n', html)
    html = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r'[\2](\1)', html)
    
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