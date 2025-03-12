import re

def code_block_remover(markdown_string: str) -> List[str]:
    """
    extracts the contents of the code block from the given Markdown string.

    Args:
        markdown_string (str): The input markdown string.

    Returns:
        list: A list of strings, each representing the content of a code block.
              Returns an empty list if no code blocks are found.
    """
    # Regular expression to match code blocks
    pattern = r'
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
        expected = ['print("Hello, World!")']
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
        expected = [
            'print("Hello, World!")',
            'console.log("Hello, World!");'
        ]
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
        expected = ['']
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

if __name__ == '__main__':
    unittest.main()