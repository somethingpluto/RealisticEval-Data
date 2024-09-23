from typing import List


def get_palindrome_list(n: int) -> List[int]:
    """
    Filter out the number of palindrome within any number n. Palindrome numbers are numbers with the same correction and reverse readings, such as 121, 1331

    Args:
        n (int): range number

    Returns:
        List[int]: Palindrome numbers
    """
    l = list(filter(lambda x: True if x == x[::-1] else False, [str(i) for i in range(n)]))
    return [int(i) for i in l]
