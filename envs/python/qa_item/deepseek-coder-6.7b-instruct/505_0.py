import re

def camel_to_snake(camel_str: str) -> str:
    """
    Convert a CamelCase string to snake_case.

    Args:
        camel_str (str): The CamelCase string to convert.

    Returns:
        str: The converted snake_case string.
    """
    # Use regular expression to find all uppercase letters that are preceded by a lowercase letter or at the start of the string
    snake_str = re.sub(r'(?<=[a-z])[A-Z]|(?<!^)[A-Z]', lambda m: '_' + m.group(0).lower(), camel_str)
    return snake_str.lower()
import unittest


class TestCamelToSnake(unittest.TestCase):
    def test_basic_conversion(self):
        """ Test basic CamelCase to snake_case conversion. """
        self.assertEqual(camel_to_snake("HelloWorld"), "hello_world")

    def test_multiple_words(self):
        """ Test conversion of a CamelCase string with multiple words. """
        self.assertEqual(camel_to_snake("ThisIsATest"), "this_is_a_test")

    def test_with_numbers(self):
        """ Test conversion with numbers in the string. """
        self.assertEqual(camel_to_snake("ConvertThis123String"), "convert_this123_string")

    def test_leading_uppercase(self):
        """ Test conversion with leading uppercase letters. """
        self.assertEqual(camel_to_snake("PythonFunction"), "python_function")

    def test_empty_string(self):
        """ Test conversion of an empty string. """
        self.assertEqual(camel_to_snake(""), "")

if __name__ == '__main__':
    unittest.main()