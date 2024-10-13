import json
from typing import Dict, Any


def parse_json_file(file_path: str) -> Dict[str, Any]:
    """
    Parses a JSON file and stores its contents in a dictionary.

    This function reads a JSON file from the specified file path, parses the JSON data, and stores
    each key-value pair from the JSON object into a dictionary.

    Args:
        file_path (str): The path to the JSON file to be parsed. The file must exist and contain valid JSON.

    Returns:
        Dict[str, Any]: A dictionary containing the key-value pairs parsed from the JSON file.
                         The function returns an empty dictionary if the file is empty.
    """
    result_dict = {}
    try:
        with open(file_path, 'r') as file:
            result_dict = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {file_path}")

    return result_dict