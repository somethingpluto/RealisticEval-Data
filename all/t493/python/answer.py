import textwrap


def wrap_content_generator(content, width=80):
    """
    Generator that yields lines of wrapped content.

    Parameters:
    - content (str): The input text content to be wrapped.
    - width (int): The maximum width for wrapping lines (default is 80).

    Yields:
    - str: Each wrapped line of text or a newline for empty lines.
    """
    for line in content.splitlines(keepends=True):
        # If the line is empty or contains only whitespace, yield a newline character.
        if line.strip() == '':
            yield '\n'
        else:
            # Wrap the non-empty line and yield each wrapped segment.
            wrapped_lines = textwrap.wrap(line, width=width)
            for wrapped_line in wrapped_lines:
                yield wrapped_line + '\n'  # Maintain line endings for wrapped lines.
