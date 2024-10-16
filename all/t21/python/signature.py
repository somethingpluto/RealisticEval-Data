from typing import List


def diff_files(file1_path: str, file2_path: str) -> List[str]:
    """
    Compare the contents of two files and print the differences in unified diff format.

    Args:
    file1_path (str): Path to the first file.
    file2_path (str): Path to the second file.

    Returns:
    List[str]: A list containing the lines of differences, if any.

    Raises:
    FileNotFoundError: If either file does not exist.
    IOError: If there is an error reading the files.
    """
