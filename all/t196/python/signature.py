from typing import List


def generate_primes(limit: int) -> List[int]:
    """
    Find all prime numbers that are less than or equal to limit using the Eichler sieve algorithm.

    Args:
        limit (int): The upper bound (inclusive) for finding prime numbers.

    Returns:
        List[int]: A list of integers containing all prime numbers less than or equal to the limit.
    """
