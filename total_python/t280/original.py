def sanitize_indents(string: str) -> str:
    """
    Given an input ``string`` with multiple lines, this function will remove all the additional indents from
    that string.

    Written by ChatGPT.

    :param string: The input string to be sanitized
    :returns: The sanitized string
    """
    lines = string.split('\n')
    # Determine minimum indent
    min_indent = float('inf')
    for line in lines:
        stripped = line.lstrip()
        if stripped != '':
            indent = len(line) - len(stripped)
            min_indent = min(min_indent, indent)

    # Remove minimum indent from all lines
    new_lines = []
    for line in lines:
        if len(line) >= min_indent:
            new_lines.append(line[min_indent:])
    return '\n'.join(new_lines)