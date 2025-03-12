
def compress_html(html: str) -> str:
    # Remove any whitespace at the beginning and end of the string
    html = html.strip()
    html = html.rstrip()

    # Remove any extra spaces in the string
    html = html.replace(r"\s+", "")

    # Convert the string to lowercase
    html = html.lower()

    # Remove any newlines in the string
    html = html.replace("\n", "")

    # Convert the string to lowercase
    return html.lower()

html_string = "<html><head><title>My Webpage</title></head><body>Hello World!</body></html>"
 compressed_html = compress_html(html_string)
print(compressed_html)  # Output: "Hello World!"

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