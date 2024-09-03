from typing import List


def code_block_remover(markdown_string: str) -> List[str]:
    """
    extracts the contents of the code block from the given Markdown string.

    Args:
        markdown_string (str): The input markdown string.

    Returns:
        list: A list of strings, each representing the content of a code block.
              Returns an empty list if no code blocks are found.
    """
