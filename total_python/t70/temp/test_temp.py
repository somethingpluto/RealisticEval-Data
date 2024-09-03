import unittest


class TestCodeBlockRemover(unittest.TestCase):

    def test_single_code_block(self):
        markdown = """
        This is a markdown with a code block.

        ```python
        print("Hello, World!")
        ```

        End of markdown.
        """
        expected = ['        print("Hello, World!")\n        ']
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

    def test_multiple_code_blocks(self):
        markdown = """
        First code block:

        ```python
        print("Hello, World!")
        ```

        Second code block:

        ```javascript
        console.log("Hello, World!");
        ```
        """
        expected = ['        print("Hello, World!")\n        ',
 '        console.log("Hello, World!");\n        ']
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

    def test_no_code_block(self):
        markdown = """
        This markdown has no code blocks.

        Just some plain text.
        """
        expected = []
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

    def test_empty_code_block(self):
        markdown = """
        Here is an empty code block:

        ```python
        ```

        End of markdown.
        """
        expected =['        ']
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

    def test_malformed_code_block(self):
        markdown = """
        This code block is missing ending:

        ```python
        print("Hello, World!")

        And some more text.
        """
        expected = []
        result = code_block_remover(markdown)
        self.assertEqual(result, expected)

import re


def code_block_remover(markdown_string):
    """
    Extracts all code block contents from a markdown string.

    Args:
        markdown_string (str): The input markdown string.

    Returns:
        list: A list of strings, each representing the content of a code block.
              Returns an empty list if no code blocks are found.
    """
    # Define a pattern that captures content within triple backticks, with optional language specifier
    pattern = r"```[a-zA-Z]*\n([\s\S]*?)```"

    # Use re.findall() to find all occurrences of the pattern
    code_blocks = re.findall(pattern, markdown_string)

    return code_blocks