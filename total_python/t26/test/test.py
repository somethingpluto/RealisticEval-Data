import unittest



class TestParseAndFormat(unittest.TestCase):

    def test_none_input(self):
        self.assertIsNone(parse_and_format(None))

    def test_list_input(self):
        self.assertEqual(parse_and_format(["apple", "banana", "cherry"]), "'apple', 'banana', 'cherry'")

    def test_string_input_with_asterisks(self):
        input_str = "* apple * banana * cherry"
        expected_output = "'apple', 'banana', 'cherry'"
        self.assertEqual(parse_and_format(input_str), expected_output)

    def test_string_input_with_commas(self):
        input_str = "apple, banana, cherry"
        expected_output = "'apple', 'banana', 'cherry'"
        self.assertEqual(parse_and_format(input_str), expected_output)

    def test_string_input_with_semicolons(self):
        input_str = "apple; banana; cherry"
        expected_output = "'apple', 'banana', 'cherry'"
        self.assertEqual(parse_and_format(input_str), expected_output)

    def test_mixed_separators(self):
        input_str = "* apple, banana; cherry"
        expected_output = "'apple', 'banana', 'cherry'"
        self.assertEqual(parse_and_format(input_str), expected_output)

    def test_multiline_input(self):
        input_str = """
        apple
        * banana
        cherry, date
        """
        expected_output = "'apple', 'banana', 'cherry', 'date'"
        self.assertEqual(parse_and_format(input_str), expected_output)