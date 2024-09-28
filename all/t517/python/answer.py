import json
import os
from typing import List, Dict, Any

def read_jsonl(file_path: str) -> List[Dict[str, Any]]:
    """
    Reads a JSON Lines file and returns its content as a list of dictionaries.

    Args:
        file_path (str): The path to the JSON Lines file.

    Returns:
        List[Dict[str, Any]]: A list of JSON objects parsed from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If there is an error parsing a line in the JSON Lines file.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    json_list = []
    with open(file_path, "r") as f:
        for line in f:
            try:
                json_obj = json.loads(line)
                json_list.append(json_obj)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(f"Error parsing line: {line.strip()} - {e}")

    return json_list
