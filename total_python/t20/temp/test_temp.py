import unittest


class TestProcessMarkdown(unittest.TestCase):
    def test_basic_asterisks(self):
        content = "*some*text*"
        expected = "*sometext*"
        self.assertEqual(process_markdown(content), expected)

    def test_nested_asterisks(self):
        content = "*some*more**complex*text**"
        expected = "*somemore complex text*"
        self.assertEqual(process_markdown(content), expected)

    def test_multiple_emphasis_blocks(self):
        content = "*hello* world, this is *some*text*"
        expected = "*hello* world, this is *sometext*"
        self.assertEqual(process_markdown(content), expected)

    def test_no_asterisks(self):
        content = "No asterisks here"
        expected = "No asterisks here"
        self.assertEqual(process_markdown(content), expected)

    def test_asterisks_with_spaces(self):
        content = "* some * *text* here *"
        expected = "* some * *text* here *"
        self.assertEqual(process_markdown(content), expected)

import re


def process_markdown(content):
    """
    Process a string to remove unnecessary inner asterisks from Markdown-like formatting,
    keeping only the outermost asterisks for emphasis.

    Args:
    content (str): A string containing the Markdown content.

    Returns:
    str: The processed Markdown content with adjusted asterisks.
    """

    # Regex to match any text enclosed with asterisks including nested ones
    regex_pattern = r'\*[^*]+\*'

    # Function to replace inner asterisks
    def replace_inner_asterisks(match):
        # Extract the matched text without the outermost asterisks
        inner_text = match.group(0)[1:-1]
        # Replace all inner asterisks with spaces
        processed_text = inner_text.replace('*', ' ')
        # Re-enclose the text with asterisks
        return '*' + processed_text + '*'

    # Use re.sub to apply the replacement function to all occurrences
    processed_content = re.sub(regex_pattern, replace_inner_asterisks, content)

    return processed_content
