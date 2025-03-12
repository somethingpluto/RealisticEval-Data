
def compress_html(html_string: str) -> str:
    """
    Compresses an HTML string by removing unnecessary whitespace without disrupting
    the integrity of content within <pre>, <div>, <script>, and <style> tags.

    For example:
        input:'  <div>   Content  </div>   '
        output: '<div> Content </div>'

    Args:
        html_string (str): The HTML content to compress.

    Returns:
        str: The compressed HTML content.
    """
    # Remove any whitespace before and after the HTML tags
    html = html.strip()
    # Remove any whitespace within the HTML tags
    html = re.sub(r'\s+', '', html)
    # Replace <pre> and <div> tags with their contents
    html = re.sub(r'<pre>(.*?)</pre>', r'<pre>(.*?)</pre>', html)
    # Replace <div> and <script> tags with their contents
    html = re.sub(r'<div>(.*?)</div>', r'<div>(.*?)</div>', html)
    # Replace <script> and <style> tags with their contents
    html = re.sub(r'<script>(.*?)</script>', r'<script>(.*?)</script>', html)
    # Replace <style> tags with their contents
    html = re.sub(r'<style>(.*?)</style>', r'<style>(.*?)</style>', html)
    # Replace <script> and <style> tags with their contents
    # (this is the last step, as we don't need to replace them in the output)
    html = html.replace('<script>', '<script>').replace('<style>', '<style>')
    return html

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