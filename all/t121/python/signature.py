from typing import List


def adjust_array_length(target_length: int, array: List) -> List:
    """
    Adjust the length of the input array according to the given target length.
    If the current length of the array is longer than the target length,
    the first part of the array is intercepted to match the target length.
    If the current length of the array is shorter than the target length,
    the elements in the array are repeated until the target length is reached.

    Args:
        target_length (int): The desired length for the array.
        array (List): The input array to be adjusted.

    Returns:
        List: A new array that has been adjusted to the target length.
    """