import re

def split_into_sentences(text):
    """
    Split the input text string into sentences.

    Args:
        text (str): The input text to be split into sentences.

    Returns:
        list: A list of sentences extracted from the input text, cleaned and stripped of leading/trailing whitespace.
    """

    # Check if the input is a string
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    # Regular expression to split the text where there is a punctuation followed by space or end of string
    # This handles situations where punctuation might be followed by a quotation mark or other punctuation
    sentence_delimiters = re.compile(r'(?<=[.!?])\s+(?=[A-Z])|(?<=[.!?]["”’])\s+(?=[A-Z])')

    # Split the text using the defined regular expression
    sentences = sentence_delimiters.split(text)

    # Remove any leading or trailing whitespace from each sentence
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # Return the cleaned list of sentences
    return sentences
