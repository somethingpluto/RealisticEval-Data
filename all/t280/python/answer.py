def dedent_text(text):
    """
    Removes excess indentation from a multiline string while preserving the relative indentation levels.

    Args:
    text (str): The multiline string to dedent.

    Returns:
    str: The dedented multiline string.
    """
    # Split the text into lines
    lines = text.splitlines()

    # Filter out blank lines for the purpose of finding the minimum indentation
    non_blank_lines = [line for line in lines if line.strip()]

    # Find the minimum indentation (excluding lines that are blank)
    min_indent = min((len(line) - len(line.lstrip()) for line in non_blank_lines), default=0)

    # Remove the minimum indentation from all lines
    dedented_lines = [line[min_indent:] if len(line) >= min_indent else line for line in lines]

    # Join the lines back into a single string with corrected indentation
    dedented_text = '\n'.join(dedented_lines)

    return dedented_text