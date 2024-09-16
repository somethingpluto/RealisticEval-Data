from typing import List


def find_json_files_with_keyword(directory:str, keyword:str) ->List[str]:
    """
    Select all json files containing the keyword from the specified directory, and return all matching json file names in the form of a list

    Args:
        directory (str): Path to the directory where JSON files are stored.
        keyword (str): Keyword to search for within the JSON files.

    Returns:
        list: A list of filenames (str) of JSON files containing the keyword.
    """