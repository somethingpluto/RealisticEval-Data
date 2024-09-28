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