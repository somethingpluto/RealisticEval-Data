from typing import List


def next_greatest_letter(letters: List[str], target: str) -> str:
    """
    Finds and returns the smallest letter in a sorted array that is larger than the given target letter.
    If the target letter is greater than or equal to all letters in the array, the function returns the first letter in the array.

    :param letters: A sorted array of letters.
    :param target: The target letter to find the next greatest letter for.
    :return: The smallest letter in the array that is larger than the target letter.
    """
    low = 0
    high = len(letters)

    # Perform binary search to find the smallest letter greater than the target
    while low < high:
        mid = (low + high) // 2
        # If the mid letter is less than or equal to the target, move to the right half
        if letters[mid] <= target:
            low = mid + 1
        else:
            # Otherwise, move to the left half
            high = mid

    # Return the letter at the calculated position, wrapping around if necessary
    return letters[low % len(letters)]
