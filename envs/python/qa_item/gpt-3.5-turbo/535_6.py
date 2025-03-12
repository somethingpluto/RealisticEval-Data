import re

def compress_html(html: str) -> str:
    html = re.sub(r'>\s+<', '><', html)
    html = re.sub(r'\s+', ' ', html)
    return html
import unittest


class TestCompressHtml(unittest.TestCase):

    def test_remove_newlines_and_tabs(self):
        input_html = """            <div>                <p>Test paragraph.</p>            </div>        """
        expected_output = '<div><p>Test paragraph.</p></div>'
        self.assertEqual(compress_html(input_html), expected_output)

    def test_replace_multiple_spaces(self):
        input_html = '<div>    <p>     Test with     multiple spaces.   </p></div>'
        expected_output = '<div><p> Test with multiple spaces. </p></div>'
        self.assertEqual(compress_html(input_html), expected_output)

    def test_remove_spaces_between_tags(self):
        input_html = '<div> <p>Test</p> </div>'
        expected_output = '<div><p>Test</p></div>'
        self.assertEqual(compress_html(input_html), expected_output)

    def test_handle_empty_input(self):
        input_html = ''
        expected_output = ''
        self.assertEqual(compress_html(input_html), expected_output)

    def test_handle_html_with_only_spaces_and_newlines(self):
        input_html = """            <div>                  </div>        """
        expected_output = '<div></div>'
        self.assertEqual(compress_html(input_html), expected_output)

if __name__ == '__main__':
    unittest.main()