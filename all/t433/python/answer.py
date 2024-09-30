def extract_paragraphs_and_lines(text: str):
    """
    Extracts paragraphs and lines from the given text.

    Args:
        text (str): The input text from which paragraphs and lines will be extracted.

    Returns:
        dict: A dictionary containing:
            - 'paragraphs': A list of paragraphs extracted from the text.
            - 'lines': A list of lines extracted from the text.
    """
    # Split the text into paragraphs
    paragraphs = text.split('\n\n')

    # Split each paragraph into lines
    lines = [line for paragraph in paragraphs for line in paragraph.split('\n')]

    # Return the extracted paragraphs and lines in a dictionary
    return {
        'paragraphs': [p.strip() for p in paragraphs if p.strip()],  # Remove empty paragraphs
        'lines': [l.strip() for l in lines if l.strip()]  # Remove empty lines
    }