import re

def compress_html(html_string: str) -> str:
    tag_pattern = r'<pre.*?>|</pre>|<div.*?>|</div>|<script.*?>|</script>|<style.*?>|</style>'
    tags = re.findall(tag_pattern, html_string, flags=re.IGNORECASE)
    
    compressed_html = ''
    in_tag = False
    for char in html_string:
        if char == '<':
            in_tag = True
        if not in_tag:
            compressed_html += char
        if char == '>':
            in_tag = False
            
    for tag in tags:
        compressed_html = compressed_html.replace(tag, tag.lstrip())
    
    return compressed_html
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