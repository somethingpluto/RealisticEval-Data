def convert(html: str) -> str:
    """
    Converts a string containing HTML to a Markdown-formatted string.

    1. Line breaks (<br> or <br/>): Replaced with newline characters.
    2. Paragraphs (<p> and </p>): Opening <p> tags are removed, while closing
        </p> tags are replaced with two newline characters to separate paragraphs.
    3. Strong emphasis (<strong> and </strong>): Replaced with double asterisks (**).
    4. Italics (<em> and </em>): Replaced with single asterisks (*).
    5. Underlined text (<u> and </u>): Replaced with single asterisks (*)
        as underlining is not supported in Markdown.
    6. Code snippets (<code> and </code>): Replaced with backticks (`).
    7. Unordered lists (<ul> and </ul>): Opening and closing tags are removed.
    8. Ordered lists (<ol> and </ol>): Opening and closing tags are removed.
    9. List items (<li>): Opening <li> tags are replaced with an asterisk followed
        by a space, while closing </li> tags are replaced with a newline character.
    10. Hyperlinks (<a href="...">...</a>): Replaced with the Markdown format
        [text](URL), where "text" is the anchor text and "URL" is the link target.

    Args:
        html (str): The input string containing HTML content.

    Returns:
        str: A string formatted in Markdown, reflecting the input HTML structure.
    """
    import re

    # Replace line breaks
    html = re.sub(r'<br\s*\/?>', '\n', html)

    # Replace paragraphs
    html = re.sub(r'<p>', '', html)
    html = re.sub(r'</p>', '\n\n', html)

    # Replace strong emphasis
    html = re.sub(r'<strong>', '**', html)
    html = re.sub(r'</strong>', '**', html)

    # Replace italics
    html = re.sub(r'<em>', '*', html)
    html = re.sub(r'</em>', '*', html)

    # Replace underlined text
    html = re.sub(r'<u>', '*', html)
    html = re.sub(r'</u>', '*', html)

    # Replace code snippets
    html = re.sub(r'<code>', '`', html)
    html = re.sub(r'</code>', '`', html)

    # Replace unordered lists
    html = re.sub(r'<ul>', '', html)
    html = re.sub(r'</ul>', '', html)

    # Replace ordered lists
    html = re.sub(r'<ol>', '', html)
    html = re.sub(r'</ol>', '', html)

    # Replace list items
    html = re.sub(r'<li>', '* ', html)
    html = re.sub(r'</li>', '\n', html)

    # Replace hyperlinks
    html = re.sub(r'<a href="([^"]*)">([^<]*)</a>', r'[\2](\1)', html)

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