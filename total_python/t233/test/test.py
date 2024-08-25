import unittest


class TestRemoveComments(unittest.TestCase):

    def test_single_line_comment(self):
        """ Test string with a comment on a single line """
        input_string = "Hello, world! # This is a comment"
        expected_output = "Hello, world! "
        self.assertEqual(remove_comments(input_string), expected_output)

    def test_multi_line_comments(self):
        """ Test string with multiple lines, each containing comments """
        input_string = "Hello, world!\n# This is a comment\nPython is fun! # another comment"
        expected_output = "Hello, world!\n\nPython is fun! "
        self.assertEqual(remove_comments(input_string), expected_output)

    def test_no_comments(self):
        """ Test string with no comments """
        input_string = "Hello, world!\nPython is fun!"
        expected_output = "Hello, world!\nPython is fun!"
        self.assertEqual(remove_comments(input_string), expected_output)

    def test_empty_string(self):
        """ Test an empty string """
        input_string = ""
        expected_output = ""
        self.assertEqual(remove_comments(input_string), expected_output)

    def test_comments_only(self):
        """ Test string where all lines are comments """
        input_string = "# comment only line\n#another comment line"
        expected_output = "\n"
        self.assertEqual(remove_comments(input_string), expected_output)
