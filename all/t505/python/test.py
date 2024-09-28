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
