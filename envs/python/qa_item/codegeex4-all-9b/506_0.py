def snake_to_camel(snake_str: str) -> str:
    """
    Convert a snake_case string to CamelCase.

    Args:
        snake_str (str): The snake_case string to convert.

    Returns:
        str: The converted CamelCase string.
    """
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)
import unittest


class TestSnakeToCamel(unittest.TestCase):
    def test_basic_conversion(self):
        """ Test basic snake_case to CamelCase conversion. """
        self.assertEqual(snake_to_camel("hello_world"), "HelloWorld")

    def test_multiple_words(self):
        """ Test conversion of a snake_case string with multiple words. """
        self.assertEqual(snake_to_camel("this_is_a_test"), "ThisIsATest")

    def test_with_numbers(self):
        """ Test conversion with numbers in the string. """
        self.assertEqual(snake_to_camel("convert_this_123_string"), "ConvertThis123String")

    def test_leading_trailing_underscores(self):
        """ Test conversion with leading and trailing underscores. """
        self.assertEqual(snake_to_camel("_leading_and_trailing_"), "LeadingAndTrailing")
        self.assertEqual(snake_to_camel("___multiple___underscores___"), "MultipleUnderscores")

    def test_empty_string(self):
        """ Test conversion of an empty string. """
        self.assertEqual(snake_to_camel(""), "")
if __name__ == '__main__':
    unittest.main()