def find_common_elements(list1, list2):
    """
    This function takes two lists as input and returns a new list containing the common elements between the two lists.
    """
    pass
import os
import tempfile
import unittest


class TestFormatText(unittest.TestCase):

    def test_basic_text(self):
        # Test with basic text
        input_text = "This is line one.\nThis is line two.\nThis is line three."
        expected_output = "This is line one. This is line two. This is line three."

        with tempfile.NamedTemporaryFile(delete=False, mode='w+t') as input_file:
            input_file.write(input_text)
            input_file.seek(0)  # Go back to the start of the file
            output_file_path = tempfile.mktemp(suffix='.txt')  # Create a temporary output file

            format_text(input_file.name, output_file_path)

            with open(output_file_path, 'r') as output_file:
                output_text = output_file.read().strip()

            self.assertEqual(expected_output, output_text)

        os.remove(input_file.name)
        os.remove(output_file_path)

    def test_single_line(self):
        # Test with a single line
        input_text = "This is a single line."
        expected_output = "This is a single line."

        with tempfile.NamedTemporaryFile(delete=False, mode='w+t') as input_file:
            input_file.write(input_text)
            input_file.seek(0)
            output_file_path = tempfile.mktemp(suffix='.txt')

            format_text(input_file.name, output_file_path)

            with open(output_file_path, 'r') as output_file:
                output_text = output_file.read().strip()

            self.assertEqual(expected_output, output_text)

        os.remove(input_file.name)
        os.remove(output_file_path)

    def test_empty_file(self):
        # Test with an empty file
        input_text = ""
        expected_output = ""

        with tempfile.NamedTemporaryFile(delete=False, mode='w+t') as input_file:
            input_file.write(input_text)
            input_file.seek(0)
            output_file_path = tempfile.mktemp(suffix='.txt')

            format_text(input_file.name, output_file_path)

            with open(output_file_path, 'r') as output_file:
                output_text = output_file.read().strip()

            self.assertEqual(expected_output, output_text)

        os.remove(input_file.name)
        os.remove(output_file_path)

    def test_file_with_no_newlines(self):
        # Test with text that has no newlines
        input_text = "This is a continuous line without breaks."
        expected_output = "This is a continuous line without breaks."

        with tempfile.NamedTemporaryFile(delete=False, mode='w+t') as input_file:
            input_file.write(input_text)
            input_file.seek(0)
            output_file_path = tempfile.mktemp(suffix='.txt')

            format_text(input_file.name, output_file_path)

            with open(output_file_path, 'r') as output_file:
                output_text = output_file.read().strip()

            self.assertEqual(expected_output, output_text)

        os.remove(input_file.name)
        os.remove(output_file_path)

if __name__ == '__main__':
    unittest.main()