def extract_paragraphs_and_lines(text: str):
    """
    Extracts paragraphs and lines from the given text.The paragraphs end with \n\n The line end with \n
    For example:
        input: First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line.
        output:

    Args:
        text (str): The input text from which paragraphs and lines will be extracted.

    Returns:
        dict: A dictionary containing:
            - 'paragraphs': A list of paragraphs extracted from the text.
            - 'lines': A list of lines extracted from the text.
    """