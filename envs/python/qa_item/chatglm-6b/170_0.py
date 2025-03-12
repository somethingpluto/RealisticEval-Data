
def convert(html: str) -> str:
    # Convert line breaks and paragraphs
    lines = html.split("\n")
    for line in lines:
        if "br" in line or "p" in line:
            lines[-1].replace("br", "\n")
            lines[-1].replace("p", "\n")

    # Convert strong emphasis, italics, and Underlined text
    for line in lines:
        if "strong" in line or "em" in line or "u" in line:
            text = line.strip()
            if text.startswith("**"):
                text = text[1:].strip()
                text = "**" + text
            elif text.startswith("*"):
                text = text[1:].strip()
                text = "*" + text
            elif text.startswith("**"):
                text = text[1:].strip()
                text = "**" + text
            elif text.startswith("*"):
                text = text[1:].strip()
                text = "*" + text

    # Convert code snippets and Unordered/Ordered lists
    for line in lines:
        if "code" in line:
            text = line.strip()
            if "code" not in lines[-1]:
                lines[-1] = text + "\n"
            else:
                lines[-1] += text + "\n"

    # Convert List items
    for line in lines:
        if "li" in line:
            text = line.strip()
            if "li" not in lines[-1]:
                lines[-1] = text + "\n"
            else:
                lines[-1] += text + "\n"

    # Convert hyperlinks
    for line in lines:
        if "a" in line:
            text = line.strip()
            if "a" not in lines[-1]:
                lines[-1] = text + "\n"
            else:
                lines[-1] += text + "\n"

    return lines[-1]

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
        expected_output = "* Item 1\n* Item 2\n"
        self.assertEqual(expected_output, convert(input_html))
    
    def test_anchor_tags(self):
        input_html = 'Check this link: <a href="http://example.com">Example</a>.'
        expected_output = 'Check this link: [Example](http://example.com).'
        self.assertEqual(expected_output, convert(input_html))
if __name__ == '__main__':
    unittest.main()