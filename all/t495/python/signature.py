import re
from typing import List


def filter_content_with_context(
        content: str,
        keywords: List[str],
        lines_before: int = 1,
        lines_after: int = 1
) -> str:
    """
    Filters website content to include lines containing any of the specified keywords as whole words,
    along with a specified number of lines before and after for context. This version uses regular expressions
    to ensure exact, whole word matching and respects case sensitivity.

    Args:
        content (str): The full text content of the website.
        keywords (List[str]): A list of strings to search for within the content.
        lines_before (int): Number of lines to include before a matching line.
        lines_after (int): Number of lines to include after a matching line.

    Returns:
        str: A string containing the filtered content with additional context.
    """
