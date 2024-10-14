from typing import List


def next_greatest_letter(letters: List[str], target: str) -> str:
    """
    Finds and returns the smallest letter in a sorted array that is larger than the given target letter.
    If the target letter is greater than or equal to all letters in the array, the function returns
    the first letter in the array.

    Args:
        letters (List[str]): A sorted array of letters (assumed to be unique and lowercase).
        target (str): The target letter to find the next greatest letter for.

    Returns:
        str: The smallest letter in the array that is larger than the target letter.
             If the target is greater than or equal to all letters, returns the first letter in the array.
    """
