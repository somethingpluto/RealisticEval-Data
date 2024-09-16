from typing import List


def read_mapping_file(mapping_file_path: str) -> List:
    """
    Reads question from the given mapping file and returns a list where each element is a tuple containing the compiled regular expression and replacement strings
    Args:
        mapping_file_path (str): Path to the file containing regex mappings.

    Returns:
        list of tuples: Each tuple contains a compiled regex object and a corresponding replacement string.
    """
