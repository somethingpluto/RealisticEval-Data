from typing import List


def classify_json_objects_by_pid(source_file: str, pid_list: List[int], match_file: str, mismatch_file: str) -> None:
    """
    read the JSON file question based on whether the pid field in the object is included in a specified pid_list. These objects are then classified into two categories based on matches and mismatches and saved in different files
    Args:
        source_file (str): Path to the source JSON file.
        pid_list (list): List of pids to match.
        match_file (str): Path to save matching objects JSON.
        mismatch_file (str): Path to save mismatching objects JSON.

    Returns:

    """
