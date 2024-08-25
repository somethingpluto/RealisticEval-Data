import unittest

class TestStringSideBySide(unittest.TestCase):

    def test_equal_length_strings(self):
        str1 = "Hello\nWorld"
        str2 = "Python\nCode"
        result = string_side_by_side(str1, str2)
        expected = "Hello                | Python              \nWorld                | Code                "
        self.assertEqual(result, expected)

    def test_first_string_longer(self):
        str1 = "Hello\nWorld\nTest"
        str2 = "Python\nCode"
        result = string_side_by_side(str1, str2)
        expected = "Hello                | Python              \nWorld                | Code                \nTest                 |                     "
        self.assertEqual(result, expected)

    def test_second_string_longer(self):
        str1 = "Hello\nWorld"
        str2 = "Python\nCode\nTest"
        result = string_side_by_side(str1, str2)
        expected = "Hello                | Python              \nWorld                | Code                \n                     | Test                "
        self.assertEqual(result, expected)

    def test_empty_first_string(self):
        str1 = ""
        str2 = "Python\nCode"
        result = string_side_by_side(str1, str2)
        expected = "                     | Python              \n                     | Code                "
        self.assertEqual(result, expected)

    def test_custom_column_width(self):
        str1 = "Hello\nWorld"
        str2 = "Python\nCode"
        result = string_side_by_side(str1, str2, column_width=10)
        expected = "Hello      | Python    \nWorld      | Code      "
        self.assertEqual(result, expected)
