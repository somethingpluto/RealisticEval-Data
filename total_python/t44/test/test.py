import unittest


class TestStringSideBySide(unittest.TestCase):

    def test_equal_length_strings(self):
        # Test with strings that have equal number of lines
        str1 = "Hello\nWorld"
        str2 = "Python\nCoding"
        expected_result = "Hello               | Python             \nWorld               | Coding             "
        result = string_side_by_side(str1, str2)
        self.assertEqual(result, expected_result)

    def test_unequal_length_strings(self):
        # Test with strings that have unequal number of lines
        str1 = "Hello\nWorld"
        str2 = "Python"
        expected_result = "Hello               | Python             \nWorld               |                    "
        result = string_side_by_side(str1, str2)
        self.assertEqual(result, expected_result)

    def test_empty_string(self):
        # Test with one empty string
        str1 = ""
        str2 = "Python\nIs\nGreat"
        expected_result = "                    | Python             \n                    | Is                 \n                    | Great              "
        result = string_side_by_side(str1, str2)
        self.assertEqual(result, expected_result)

    def test_variable_column_width(self):
        # Test with a specific column width
        str1 = "Short"
        str2 = "This is a much longer line"
        expected_result = "Short               | This is a much longe"
        result = string_side_by_side(str1, str2, 20)
        self.assertEqual(result, expected_result)

    def test_all_empty_strings(self):
        # Test with all empty strings
        str1 = ""
        str2 = ""
        expected_result = ""
        result = string_side_by_side(str1, str2)
        self.assertEqual(result, expected_result)