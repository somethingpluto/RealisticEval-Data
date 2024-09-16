from typing import Union


def find_largest_divisible(n: int) -> Union[int, None]:
    """
    find the largest integer between a given number n and half of it that is divisible by 10 or 5
    Args:
        n (int): The upper bound of the range.

    Returns:
        The largest integer between n and half of n that is divisible by 5, or
         None if no such number exists.
    """
