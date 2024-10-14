from typing import List


def parse_git_diff(diff_text: str) -> List:
    """
    Parses a string containing the contents of a Git diff and returns a list of objects
    detailing the changes for each file.

    Args:
        diff_text (str): The Git diff text to parse.

    Returns:
        list: A list of objects representing the diff for each file, where each object contains
              details about the changes, such as file name, added lines, and removed lines.
    """