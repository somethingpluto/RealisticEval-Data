from typing import Tuple


def get_min_seq_num_and_distance(file_path: str, word1: str, word2: str) -> Tuple[int, int]:
    """
    Finds the minimum distance between two words in a text file, considering each line as a separate sequence.
    Args:
        file_path (str): The path to the file to read.
        word1 (str): The first word to search for.
        word2 (str): The second word to search for.

    Returns:
        tuple: A tuple containing the line number with the minimum distance and the minimum distance itself.
          Returns (None, float('inf')) if one or both words are not found in any line.
    """
