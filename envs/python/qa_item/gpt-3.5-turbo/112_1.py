import re

def convert_html_headings_to_markdown(html: str) -> str:
    headings = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    
    for index, heading in enumerate(headings):
        html = re.sub(rf'<{heading}>(.*?)</{heading}>', f'{"#"*(index+1)} \\1\n', html, flags=re.IGNORECASE)
    
    return html
import unittest


class TestConvertHtmlHeadingsToMarkdown(unittest.TestCase):

    def test_convert_h1_to_markdown(self):
        input_html = '<h1>This is a Heading 1</h1>'
        expected_output = '# This is a Heading 1'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h2_to_markdown(self):
        input_html = '<h2>This is a Heading 2</h2>'
        expected_output = '## This is a Heading 2'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h3_to_markdown(self):
        input_html = '<h3>This is a Heading 3</h3>'
        expected_output = '### This is a Heading 3'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h4_to_markdown(self):
        input_html = '<h4>This is a Heading 4</h4>'
        expected_output = '#### This is a Heading 4'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h5_to_markdown(self):
        input_html = '<h5>This is a Heading 5</h5>'
        expected_output = '##### This is a Heading 5'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

    def test_convert_h6_to_markdown(self):
        input_html = '<h6>This is a Heading 6</h6>'
        expected_output = '###### This is a Heading 6'
        self.assertEqual(convert_html_headings_to_markdown(input_html), expected_output)

if __name__ == '__main__':
    unittest.main()