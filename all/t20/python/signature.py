import re


def process_markdown_file(file_path):
    """Process the contents of a Markdown file to remove unnecessary asterisks.

    Args:
        file_path (str): The path to the Markdown file.

    Returns:
        str: The processed Markdown content with only outermost asterisks retained.
    """