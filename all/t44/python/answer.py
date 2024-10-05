from typing import Tuple


def align_lines_left(str1: str, str2: str) -> Tuple[str,str]:
    """
    Align two lines of string to the left, supplementing with Spaces if the length is not enough

    Args:
        str1 (str): str1
        str2 (str): str2

    Returns:
        Tuple[str]: aligned str1 aligned str2
    """

    # Determine the maximum length of the two strings
    max_length = max(len(str1), len(str2))

    # Align both strings to the left by padding with spaces
    aligned_str1 = str1.ljust(max_length)
    aligned_str2 = str2.ljust(max_length)

    return aligned_str1, aligned_str2
