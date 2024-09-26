from typing import List


def min_removals_to_make_unique(nums: List[int]) -> int:
    """
    Given an integer array, calculate the minimum number of elements to delete so that the elements in the array are not duplicate.
    For example:
        input: [3, 3, 1, 2, 2, 1]
        output: 3

    Args:
        nums (List[int]): integer array of nums

    Returns:
        minimum number of moves to make every value in nums unique
    """
