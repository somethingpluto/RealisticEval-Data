import re


def process_markdown_file(file_path):
    """Process the contents of a Markdown file to remove unnecessary asterisks.

    Args:
        file_path (str): The path to the Markdown file.

    Returns:
        str: The processed Markdown content with only outermost asterisks retained.
    """
    # Read the contents of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Function to replace asterisks while keeping only the outermost
    def remove_inner_asterisks(text):
        # This regex will find all occurrences of asterisks and 
        # retain only the outermost ones
        return re.sub(r'(\*+)(?=(\*+))', '', text)

    # Process the content
    processed_content = remove_inner_asterisks(content)

    # Return the processed content
    return processed_content