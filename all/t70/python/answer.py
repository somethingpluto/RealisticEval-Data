import re
from typing import List


def code_block_remover(markdown_string: str) -> List[str]:
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
