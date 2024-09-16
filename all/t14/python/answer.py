import json
import os
from typing import List


def find_json_files_with_keyword(directory:str, keyword:str) ->List[str]:
    """
    Search all JSON files in the specified directory for a given keyword
    and return a list of filenames that contain the keyword.

    Args:
        directory (str): Path to the directory where JSON files are stored.
        keyword (str): Keyword to search for within the JSON files.

    Returns:
        list: A list of filenames (str) of JSON files containing the keyword.
    """
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    if keyword in json.dumps(data):
                        matching_files.append(file)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return matching_files
