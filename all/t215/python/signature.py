def replace_words_in_file(file_path: str, replacement_dict: dict) -> str:
    """
    Read a text file, replace words according to a dictionary map, and return the modified text.

    Parameters:
    - file_path (str): The path to the text file.
    - replacement_dict (dict): A dictionary where the keys are words to be replaced, and the values are the replacement words.

    Returns:
    - str: The text with the words replaced.
    """
