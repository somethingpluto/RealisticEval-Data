def remove_comments(string: str) -> str:
    """
    Removes comments from the provided string. Comments start with a '#' and end at the newline.

    Args:
        string (str): The input string containing potential comments.

    Returns:
        str: The string with all comments removed.
    """
    # Split the string by newline characters
    lines = string.split('\n')
    
    # Iterate through each line and remove comments
    cleaned_lines = [line.split('#')[0] for line in lines]
    
    # Join the cleaned lines back into a single string
    cleaned_string = '\n'.join(cleaned_lines)
    
    return cleaned_string
import unittest


class TestRemoveComments(unittest.TestCase):

    def test_single_line_comment(self):
        """ Test string with a comment on a single line """
        input_string = "Hello, world!# This is a comment"
        expected_output = "Hello, world!"
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

if __name__ == '__main__':
    unittest.main()