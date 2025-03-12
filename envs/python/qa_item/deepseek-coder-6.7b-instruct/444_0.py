def format_comment(string, max_length=60):
    """
    Formats a string into a commented block with specified maximum line length.

    Args:
        string (str): The input string to format.
        max_length (int): Maximum length of each line in the output.

    Returns:
        str: A formatted string with each line prefixed by '# ' and not exceeding the specified max_length.
    """
    # Initialize the result list to store formatted lines
    result = []
    
    # Split the input string into words
    words = string.split()
    
    # Initialize the current line with the comment prefix
    current_line = "# "
    
    # Iterate over each word
    for word in words:
        # Check if adding the word to the current line exceeds the max_length
        if len(current_line) + len(word) + 1 > max_length:
            # If it does, add the current line to the result and start a new line
            result.append(current_line)
            current_line = "# "
        
        # Add the word to the current line
        current_line += word + " "
    
    # Add the last line to the result
    result.append(current_line)
    
    # Join the result list into a single string with newline characters
    return "\n".join(result)
import unittest


class TestFormatComment(unittest.TestCase):

    def test_short_string(self):
        """Test with a short string that fits within max_length"""
        input_string = "This is a test."
        expected_output = "# This is a test."
        self.assertEqual(format_comment(input_string), expected_output)

    def test_long_string(self):
        """Test with a longer string that exceeds max_length"""
        input_string = "This is a test of the format_comment function which should wrap long lines correctly."
        expected_output = (
            "# This is a test of the format_comment function which should\n"
            "# wrap long lines correctly."
        )
        self.assertEqual(format_comment(input_string, max_length=60), expected_output)

    def test_multiple_lines(self):
        """Test with multiple lines of input"""
        input_string = "First line.\nSecond line that is quite long and needs to be wrapped."
        expected_output = (
            "# First line.\n"
            "# Second line that is quite long and needs to be wrapped."
        )
        self.assertEqual(format_comment(input_string, max_length=60), expected_output)

    def test_exact_max_length(self):
        """Test with a line that is exactly max_length characters long"""
        input_string = "A" * 60  # 60 characters long
        expected_output = "# " + "A" * 60
        self.assertEqual(format_comment(input_string, max_length=60), expected_output)

    def test_empty_string(self):
        """Test with an empty string"""
        input_string = ""
        expected_output = "# "
        self.assertEqual(format_comment(input_string), expected_output)

if __name__ == '__main__':
    unittest.main()