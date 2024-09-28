import re


def filter_content_with_context(content, keywords, lines_before=1, lines_after=1):
    """
    Filters website content to include lines containing any of the specified keywords as whole words,
    along with a specified number of lines before and after for context. This version uses regular expressions
    to ensure exact, whole word matching and respects case sensitivity.

    Parameters:
    - content: The full text content of the website.
    - keywords: An array of strings to search for within the content.
    - lines_before: Number of lines to include before a matching line.
    - lines_after: Number of lines to include after a matching line.

    Returns:
    A string containing the filtered content with additional context.
    """
    lines = content.splitlines()
    matched_lines = set()

    for i, line in enumerate(lines):
        for keyword in keywords:
            # Use a regular expression to find whole word matches with exact case
            if re.search(r'\b' + re.escape(keyword) + r'\b', line):
                context_range = range(max(i - lines_before, 0), min(i + lines_after + 1, len(lines)))
                matched_lines.update(context_range)

    # Extract the matched lines and their context
    filtered_lines = [lines[i] for i in sorted(matched_lines)]

    # Join the filtered lines back into a single string
    filtered_content = "\n".join(filtered_lines)

    return filtered_content