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