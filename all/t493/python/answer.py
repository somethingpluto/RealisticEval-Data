import textwrap


def wrap_content_generator(content, width=80):
    """Wrap the text content to the specified maximum width and generate these lines line by line


    Args:
        content (str): The content to be wrapped and yielded line by line.
        width (int): The maximum width of the lines, default is 80 characters.

    Yields:
        str: Each line of the content wrapped to the specified width.
    """
    for line in content.splitlines(keepends=True):
        if line.strip() == '':  # Check if the line is essentially empty.
            yield '\n'
        else:
            for line2 in textwrap.wrap(line, width=width):
                yield line2