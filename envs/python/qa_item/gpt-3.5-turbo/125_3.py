import re

def compress_html(html_string: str) -> str:
    def compress(match):
        return re.sub(r'\s+', ' ', match.group(0))

    return re.sub(r'(?<=\s)(?![^<]*>|[^<]*<\/(?:pre|div|script|style)>)(?![^<]*>|[^<]*<\/(?:pre|div|script|style)>)(?![^<]*>|[^<]*<\/(?:pre|div|script|style)>)(?![^<]*>|[^<]*<\/(?:pre|div|script|style)>)\s+(?=[^<]*|(?![^<]*>|<\/(?:pre|div|script|style)>)[^<]*>|(?![^<]*>|<\/(?:pre|div|script|style)>)[^<]*>|(?![^<]*>|<\/(?:pre|div|script|style)>)[^<]*>|(?![^<]*>|<\/(?:pre|div|script|style)>)[^<]*>)', compress, html_string)
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