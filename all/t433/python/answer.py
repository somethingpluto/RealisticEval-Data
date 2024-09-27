def read_paragraphs(filename):
    """
    Reads the contents of a specified text file and splits it into paragraphs and lines.

    Args:
        filename (str): The path to the text file to be read.

    Returns:
        list: A nested list where each sublist contains lines of a paragraph.
    """
    with open(filename, 'r') as file:
        # Read the entire content of the file
        content = file.read()

        # Split content into paragraphs based on two newlines
        paragraphs = content.split('\n\n')

        # Split each paragraph into lines based on one newline
        return [paragraph.split('\n') for paragraph in paragraphs]