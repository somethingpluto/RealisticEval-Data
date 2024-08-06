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