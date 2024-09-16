def remove_common_indentation(multiline_text: str) -> str:
    """
    Removes the common leading indentation from each line in a given multi-line string,
    preserving the relative indentation of the text.

    Args:
        multiline_text (str): The input string containing multiple lines.

    Returns:
        str: The sanitized string with common leading indentation removed.
    """
    lines = multiline_text.split('\n')

    # Filter out lines that are empty or only whitespace, as they do not affect minimum indentation
    non_empty_lines = [line for line in lines if line.strip() != '']

    # Determine the minimum indentation of non-empty lines
    min_indent = float('inf')
    for line in non_empty_lines:
        stripped_line = line.lstrip()
        indent = len(line) - len(stripped_line)
        min_indent = min(min_indent, indent)

    # If there's no indentation or all lines are empty, return the original string
    if min_indent == float('inf'):
        return multiline_text

    # Remove the common leading indentation from each line
    sanitized_lines = [line[min_indent:] for line in lines]

    return '\n'.join(sanitized_lines)
