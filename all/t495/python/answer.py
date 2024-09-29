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

    Parameters:
    - content (str): The full text content of the website.
    - keywords (List[str]): A list of strings to search for within the content.
    - lines_before (int): Number of lines to include before a matching line.
    - lines_after (int): Number of lines to include after a matching line.

    Returns:
    str: A string containing the filtered content with additional context.
    """

    # Split the content into individual lines
    lines = content.splitlines()
    matched_lines = set()  # Use a set to avoid duplicate lines

    # Iterate over each line to find matches
    for i, line in enumerate(lines):
        for keyword in keywords:
            # Use a regular expression to find whole word matches with exact case
            if re.search(r'\b' + re.escape(keyword) + r'\b', line):
                # Determine the range of lines to include for context
                context_range = range(max(i - lines_before, 0), min(i + lines_after + 1, len(lines)))
                matched_lines.update(context_range)  # Add the context lines to the set

    # Extract the matched lines and their context, sorted by their original order
    filtered_lines = [lines[i] for i in sorted(matched_lines)]

    # Join the filtered lines back into a single string
    filtered_content = "\n".join(filtered_lines)

    return filtered_content