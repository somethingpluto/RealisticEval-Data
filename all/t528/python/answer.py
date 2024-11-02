import os


def find_markdown_files(dir_path):
    """
    Recursively searches for Markdown files in the specified directory.

    Args:
        dir_path (str): The directory path to search in.

    Returns:
        list: A list of paths to Markdown files.
    """
    markdown_files = []

    # Read the contents of the directory
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            # If it's a Markdown file, add it to the list
            if file_path.endswith('.md'):
                markdown_files.append(file_path)

    return markdown_files