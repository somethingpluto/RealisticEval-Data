from typing import List


def two_sum(nums: List[int], target: int) -> int:
    """
    Finds two indices of numbers in the array that sum up to the target value.

    Args:
        nums (List[int]): The input array of integers.
        target (int): The target sum value.

    Returns:
        list[int]: A list containing the indices of the two numbers.

    Raises:
        ValueError: If no such indices are found.
    """
