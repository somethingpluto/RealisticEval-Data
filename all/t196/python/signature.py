def generate_primes(limit: int) -> list[int]:
    """
    Find all prime numbers that are less than or equal to limit using the Eichler sieve algorithm.

    :param limit: The upper bound (inclusive) for finding prime numbers.
    :return: A list of integers containing all prime numbers less than or equal to the limit.
    :raises ValueError: If the limit is less than 2.
    """