import unittest


class TestStringSideBySide(unittest.TestCase):
    def test_equal_length_strings(self):
        s1 = "Hello\nWorld"
        s2 = "Test\nCase"
        expected = "Hello               | Test               \nWorld               | Case               "
        self.assertEqual(string_side_by_side(s1, s2), expected)

    def test_unequal_length_strings(self):
        s1 = "Short"
        s2 = "A much longer string\nacross multiple lines"
        expected = "Short               | A much longer string\n                    | across multiple lines"
        self.assertEqual(string_side_by_side(s1, s2), expected)

    def test_empty_first_string(self):
        s1 = ""
        s2 = "Non-empty"
        expected = "                    | Non-empty          "
        self.assertEqual(string_side_by_side(s1, s2), expected)

    def test_empty_second_string(self):
        s1 = "Non-empty"
        s2 = ""
        expected = "Non-empty          |                    "
        self.assertEqual(string_side_by_side(s1, s2), expected)

    def test_special_characters(self):
        s1 = "Special: #@!"
        s2 = "Characters: %^&*"
        expected = "Special: #@!        | Characters: %^&*   "
        self.assertEqual(string_side_by_side(s1, s2), expected)
def string_side_by_side(string1, string2, column_width=20):
    # Split the strings into lists of lines
    lines1 = string1.splitlines()
    lines2 = string2.splitlines()

    # Find the maximum length of the two lists
    max_length = max(len(lines1), len(lines2))

    # Pad both lists to have the same number of lines
    padded_lines1 = [line.ljust(column_width) for line in lines1] + [' ' * column_width] * (max_length - len(lines1))
    padded_lines2 = [line.ljust(column_width) for line in lines2] + [' ' * column_width] * (max_length - len(lines2))

    # Use a list comprehension to format and concatenate lines
    formatted_lines = [f"{line1} | {line2}" for line1, line2 in zip(padded_lines1, padded_lines2)]

    # Join all formatted lines into a single string
    return '\n'.join(formatted_lines)
