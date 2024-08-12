import unittest


class TestExtractCodeBlocks(unittest.TestCase):
    def test_single_code_block(self):
        """Test extraction from a string containing a single code block."""
        markdown = "```python\ndef hello_world():\n    print(\"Hello, world!\")\n```"
        self.assertEqual(extract_code_blocks(markdown), ["def hello_world():\n    print(\"Hello, world!\")"])

    def test_multiple_code_blocks(self):
        """Test extraction from a string containing multiple code blocks."""
        markdown = """
        ```python
        def hello_world():
            print("Hello, world!")
        ```
        Here's some text.
        ```javascript
        function hello() {
            console.log("Hello!");
        }
        ```
        """
        expected = ['def hello_world():\n            print("Hello, world!")',
                    'function hello() {\n            console.log("Hello!");\n        }']
        self.assertEqual(extract_code_blocks(markdown), expected)

    def test_no_code_blocks(self):
        """Test a string with no code blocks to ensure it returns an empty list."""
        markdown = "This is a simple paragraph without any code."
        self.assertEqual(extract_code_blocks(markdown), [])

    def test_nested_code_blocks(self):
        """Test a string where code blocks are 'nested' in quotes, but not really nested."""
        markdown = """
        "```
        Code block inside quotes
        ```"
        ```
        Actual code block
        ```
        """
        expected = [
            "Code block inside quotes",
            "Actual code block"
        ]
        self.assertEqual(extract_code_blocks(markdown), expected)

    def test_code_block_with_extra_backticks(self):
        """Test a string where the code block has more than three backticks."""
        markdown = "````python\ndef extra_backticks():\n    print(\"Too many backticks!\")\n````"
        self.assertEqual(extract_code_blocks(markdown), ["def extra_backticks():\n    print(\"Too many backticks!\")"])
