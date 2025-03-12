import textwrap

def wrap_content_generator(content: str, width=80):
    """
    Wrap the text content to the specified maximum width and generate these lines line by line

    Args:
        content (str): The content to be wrapped and yielded line by line.
        width (str): The maximum width of the lines, default is 80 characters.

    Yields:
        str: Each line of the content wrapped to the specified width.
    """
    wrapper = textwrap.TextWrapper(width=width)
    for line in content.split('\n'):
        yield from wrapper.wrap(line)
import unittest


class TestWrapContentGenerator(unittest.TestCase):

    def test_empty_content(self):
        """Test with empty content."""
        result = list(wrap_content_generator(""))
        self.assertEqual(result, [])

    def test_single_line_content(self):
        """Test with a single line of content within default width."""
        result = list(wrap_content_generator("Hello, world!"))
        self.assertEqual(result, ["Hello, world!"])

    def test_multi_line_content(self):
        """Test with multiple lines of content each fitting within default width."""
        content = "Hello\nWorld\nPython"
        result = list(wrap_content_generator(content))
        self.assertEqual(result, ["Hello", "World", "Python"])

    def test_long_line(self):
        """Test with a single long line that exceeds the default width."""
        content = "This is a very long line that should definitely be wrapped around the default width of 80 characters."
        result = list(wrap_content_generator(content))
        self.assertTrue(len(max(result, key=len)) <= 80)

    def test_custom_width(self):
        """Test with a custom width."""
        content = "This is a test for custom width setting."
        result = list(wrap_content_generator(content, width=10))
        self.assertTrue(all(len(line) <= 10 for line in result))

    def test_only_whitespaces(self):
        """Test content that contains only whitespace characters."""
        result = list(wrap_content_generator("     "))
        self.assertEqual(result, ["\n"])
if __name__ == '__main__':
    unittest.main()