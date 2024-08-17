import unittest


class TestProcessMarkdown(unittest.TestCase):

    def test_simple_case(self):
        # Test with simple asterisks case
        self.assertEqual(process_markdown("*some*text*"), "*sometime *")

    def test_multiple_asterisks_case(self):
        # Test with multiple asterisks surrounding the text
        self.assertEqual(process_markdown("***bold**text*"), "*boldtext*")

    def test_no_asterisks_case(self):
        # Test with no asterisks in the text
        self.assertEqual(process_markdown("plain text"), "plain text")

    def test_nested_asterisks_case(self):
        # Test with nested asterisks in the text
        self.assertEqual(process_markdown("*nest*ed*text*"), "*nestedtext*")

    def test_outermost_asterisks_case(self):
        # Test with multiple layers of outer asterisks
        self.assertEqual(process_markdown("****outer**most*"), "*outermost*")

import re


def process_markdown(content):
    """
    Processes the content of a Markdown string by removing unnecessary asterisks
    and keeping only the outermost asterisks.

    Parameters:
    - content (str): The content of the Markdown file as a string.

    Returns:
    - str: The processed content with only outermost asterisks kept.
    """

    def remove_inner_asterisks(match):
        # Extract the text within the asterisks and remove any inner asterisks
        text = match.group(0)
        cleaned_text = re.sub(r'\*+', '', text.strip('*'))
        return f"*{cleaned_text}*"

    # Regex pattern to match text surrounded by asterisks
    pattern = re.compile(r'\*+([^*]+)\*+')

    # Apply the function to replace the inner asterisks with clean text
    result = pattern.sub(remove_inner_asterisks, content)

    return result