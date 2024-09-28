import unittest


class TestFormatStrFunction(unittest.TestCase):

    def test_case_1(self):
        # Test with a regular string input
        input_data = "This is a test.\nAnd here is some text."
        expected_output = "> This is a test.\n> And here is some text."
        self.assertEqual(format_str(input_data), expected_output)

    def test_case_2(self):
        # Test with an integer input
        input_data = 12345
        expected_output = "> 12345"
        self.assertEqual(format_str(input_data), expected_output)

    def test_case_3(self):
        # Test with an unbalanced code block
        input_data = "Here is some code:\n```\nprint('Hello, World!')\n"
        expected_output = "> Here is some code:\n> ```\n> print('Hello, World!')\n> ```"
        self.assertEqual(format_str(input_data), expected_output)

    def test_case_4(self):
        # Test with a list input
        input_data = ["Line 1", "Line 2", "Line 3"]
        expected_output = "> Line 1\n> Line 2\n> Line 3"
        self.assertEqual(format_str(input_data), expected_output)

    def test_case_5(self):
        # Test with an already formatted Markdown input
        input_data = "> This is already a quote.\n> But here's some code:\n```\nprint('Test')\n```"
        expected_output = "> This is already a quote.\n> But here's some code:\n> ```\n> print('Test')\n> ```"
        self.assertEqual(format_str(input_data), expected_output)
