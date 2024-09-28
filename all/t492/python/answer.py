def format_content(content):
    """
    Format the given content by removing extra blank lines and spaces.

    :param content: A string containing the text to be formatted.
    :return: A formatted string.
    """
    # Split the content into lines
    lines = content.splitlines()

    # Remove extra spaces and blank lines
    formatted_lines = []
    for line in lines:
        # Strip leading and trailing spaces
        stripped_line = line.strip()
        # Only add non-empty lines or a single blank line
        if stripped_line:
            formatted_lines.append(stripped_line)
        elif formatted_lines and formatted_lines[-1]:  # Ensure we only add a single blank line
            formatted_lines.append("")

    # Join lines back into a single string, ensuring single spaces between words
    formatted_content = "\n".join(formatted_lines)
    # Replace multiple spaces with a single space
    formatted_content = ' '.join(formatted_content.split())

    return formatted_content