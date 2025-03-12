import re

def find_placeholders(text):
    """
    Find and return a list of all placeholders in the format {{ placeholder }} from the input text.

    Args:
        text (str): The input string containing potential placeholders.

    Returns:
        list: A list of matching placeholders.
    """
    return re.findall(r'\{\{(.+?)\}\}', text)
import unittest


class TestFindPlaceholders(unittest.TestCase):

    def test_multiple_placeholders(self):
        """Test string with multiple placeholders."""
        input_text = "Here are some placeholders: {{ placeholder1 }}, {{ placeholder2 }}, and {{ placeholder3 }}."
        expected_output = ['placeholder1', 'placeholder2', 'placeholder3']
        self.assertEqual(find_placeholders(input_text), expected_output)

    def test_no_placeholders(self):
        """Test string with no placeholders."""
        input_text = "This string has no placeholders."
        expected_output = []
        self.assertEqual(find_placeholders(input_text), expected_output)

    def test_single_placeholder(self):
        """Test string with a single placeholder."""
        input_text = "The only placeholder is {{ singlePlaceholder }}."
        expected_output = ['singlePlaceholder']
        self.assertEqual(find_placeholders(input_text), expected_output)

    def test_placeholder_with_spaces(self):
        """Test string with placeholders that have extra spaces."""
        input_text = "Placeholders with spaces: {{  placeholder_with_spaces  }} and {{ placeholder2 }}."
        expected_output = ['placeholder_with_spaces', 'placeholder2']
        self.assertEqual(find_placeholders(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()