def replace_words_in_file(file_path, replacement_dict):
    """
    Read a text file, replace words according to a dictionary map, and return the modified text.

    Parameters:
    - file_path (str): The path to the text file.
    - replacement_dict (dict): A dictionary where the keys are words to be replaced, and the values are the replacement words.

    Returns:
    - str: The text with the words replaced.
    """
    try:
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Replace words according to the replacement dictionary
        for old_word, new_word in replacement_dict.items():
            text = text.replace(old_word, new_word)

        return text

    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"Error: {str(e)}"