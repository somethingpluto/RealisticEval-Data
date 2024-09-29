import textwrap
from typing import Generator


def wrap_content_generator(content: str, width: int = 80) -> Generator[str, None, None]:
    """
    A generator function that yields wrapped lines from the given content.

    Args:
        content (str): The content to be wrapped.
        width (int): The maximum width of each wrapped line. Default is 80 characters.

    Yields:
        str: Each wrapped line of text, preserving empty lines.
    """
    for line in content.splitlines(keepends=True):
        # Check if the line is empty or contains only whitespace
        if line.strip() == '':
            yield '\n'  # Preserve empty lines as they are
        else:
            # Wrap the non-empty line according to the specified width
            for wrapped_line in textwrap.wrap(line, width=width):
                yield wrapped_line  # Yield each wrapped line