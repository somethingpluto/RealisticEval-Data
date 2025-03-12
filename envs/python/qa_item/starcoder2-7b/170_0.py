import re

def convert(html: str) -> str:
    # Replace <br> and <br/> with newline characters
    html = re.sub(r'(<br\s*/?>)', '\n', html)

    # Replace <p> and </p> with newline characters
    html = re.sub(r'(</p>)', '\n\n', html)
    html = re.sub(r'(<p>)', '', html)

    # Replace <strong> and </strong> with double asterisks
    html = re.sub(r'(</strong>)', '**', html)
    html = re.sub(r'(<strong>)', '**', html)

    # Replace <em> and </em> with single asterisks
    html = re.sub(r'(</em>)', '*', html)
    html = re.sub(r'(<em>)', '*', html)

    # Replace <u> and </u> with single asterisks
    html = re.sub(r'(</u>)', '*', html)
    html = re.sub(r'(<u>)', '*', html)

    # Replace <code> and </code> with backticks
    html = re.sub(r'(</code>)', '`', html)
    html = re.sub(r'(<code>)', '`', html)

    # Remove <ul> and </ul>
    html = re.sub(r'(</ul>)', '', html)
    html = re.sub(r'(<ul>)', '', html)

    # Remove <ol> and </ol>
    html = re.sub(r'(</ol>)', '', html)
    html = re.sub(r'(<ol>)', '', html)

    # Replace <li> with an asterisk followed by a space
    html = re.sub(r'(<li>)', '* ', html)

    # Replace <a href="...">...</a> with the Markdown format [text](URL)
    html = re.sub(r'(<a href=")(.*?)(">)(.*?)(</a>)', r'[\4](\2)', html)

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