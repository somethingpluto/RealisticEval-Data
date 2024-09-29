def save_content_to_file(content: str, path: str) -> None:
    """
    Saves the provided content to a specified file after cleaning up
    redundant whitespace.

    Args:
        content (str): The text content to be saved to the file.
        path (str): The file path where the content will be saved.

    Returns:
        None
    """
    # Remove redundant whitespace from the content.
    # Split the content into lines, strip leading/trailing whitespace,
    # and filter out empty lines.
    content = '\n'.join(line.strip() for line in content.splitlines() if line.strip())

    # Replace multiple spaces with a single space.
    content = ' '.join(content.split())

    # Write the cleaned content to the specified file.
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
