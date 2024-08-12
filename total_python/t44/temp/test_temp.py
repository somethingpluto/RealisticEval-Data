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
def string_side_by_side(string1, string2, column_width=20):
    lines1 = string1.splitlines()
    lines2 = string2.splitlines()

    max_length = max(len(lines1), len(lines2))
    lines1 += [''] * (max_length - len(lines1))
    lines2 += [''] * (max_length - len(lines2))

    formatted_lines = (f"{line1:<{column_width}} | {line2:<{column_width}}"
                       for line1, line2 in zip(lines1, lines2))

    return '\n'.join(formatted_lines)
