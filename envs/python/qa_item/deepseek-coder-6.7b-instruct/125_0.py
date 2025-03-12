import re

def compress_html(html_string: str) -> str:
    """
    Compresses an HTML string by removing unnecessary whitespace without disrupting
    the integrity of content within <pre>, <div>, <script>, and <style> tags.

    Args:
        html_string (str): The HTML content to compress.

    Returns:
        str: The compressed HTML content.
    """
    
    # Regular expression to match the tags we want to preserve whitespace within
    preserve_tags = re.compile(r'<(pre|div|script|style)[^>]*>.*?</\1>', re.DOTALL)
    
    # Function to compress the content outside of the preserved tags
    def compress_content(content):
        return re.sub(r'\s+', ' ', content).strip()
    
    # Find all preserved tags and their positions
    preserved_tags = []
    for match in preserve_tags.finditer(html_string):
        preserved_tags.append((match.start(), match.end(), match.group(0)))
    
    # If there are no preserved tags, compress the entire string
    if not preserved_tags:
        return compress_content(html_string)
    
    # Compress the content outside of the preserved tags
    compressed_html = []
    last_end = 0
    
    for start, end, tag in preserved_tags:
        # Compress the content before the preserved tag
        compressed_html.append(compress_content(html_string[last_end:start]))
        # Append the preserved tag as is
        compressed_html.append(tag)
        last_end = end
    
    # Compress the remaining content after the last preserved tag
    compressed_html.append(compress_content(html_string[last_end:]))
    
    # Join the compressed parts and return the result
    return ''.join(compressed_html)
import unittest


class TestCompressHTML(unittest.TestCase):

    def test_remove_leading_and_trailing_spaces_around_tags(self):
        input_html = '  <div>  <p>Test</p>  </div>  '
        expected = '<div><p>Test</p></div>'
        self.assertEqual(compress_html(input_html), expected)

    def test_replace_multiple_newlines_with_single_space(self):
        input_html = '<div>\n\n<p>Test</p>\n\n</div>'
        expected = '<div> <p>Test</p> </div>'
        self.assertEqual(compress_html(input_html), expected)

    def test_remove_unnecessary_spaces_within_text(self):
        input_html = '<p>This    is a test</p>'
        expected = '<p>This is a test</p>'
        self.assertEqual(compress_html(input_html), expected)

    def test_handle_empty_strings(self):
        input_html = ''
        expected = ''
        self.assertEqual(compress_html(input_html), expected)

    def test_process_complex_nested_html_correctly(self):
        input_html = '<div>   <span>    Text <i>    Italic </i> more text </span>   </div>'
        expected = '<div><span>Text <i>Italic</i> more text</span></div>'
        self.assertEqual(compress_html(input_html), expected)

    def test_not_disrupt_content_within_pre_and_textarea_tags(self):
        input_html = '<pre>\n    function example() {\n        console.log("example");\n    }\n</pre>'
        expected = '<pre>\n    function example() {\n        console.log("example");\n    }\n</pre>'
        self.assertEqual(compress_html(input_html), expected)

    def test_handle_html_with_attributes_correctly(self):
        input_html = '<a href="http://example.com"    title="Example" >Link</a>'
        expected = '<a href="http://example.com" title="Example">Link</a>'
        self.assertEqual(compress_html(input_html), expected)

if __name__ == '__main__':
    unittest.main()