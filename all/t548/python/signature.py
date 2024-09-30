import json


def read_txt_add_json_bracket(filename:str):
    """
    Reads a text file, wraps its content in JSON brackets, and parses it into a Python object.

    Args:
        filename (str): The path to the text file to be read.

    Returns:
        list: A list parsed from the JSON content wrapped in brackets.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the content cannot be parsed as JSON.
    """