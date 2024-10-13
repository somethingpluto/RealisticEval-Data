from typing import Dict, Any


def parse_json_file(file_path: str) -> Dict[str, Any]:
    """
    Parses a JSON file and stores its contents in a dictionary.

    Args:
        file_path (str): The path to the JSON file to be parsed. The file must exist and contain valid JSON.
                      The path should be a fully qualified path or relative to the current working directory.

    Returns:
        Dict[str, Any]: A dictionary containing the key-value pairs parsed from the JSON file.
    """