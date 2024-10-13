from typing import List


def generate_primes(limit: int) -> List[int]:
    """
    Find all prime numbers that are less than or equal to limit using the Sieve of Eratosthenes algorithm.

    :param limit: The upper bound (inclusive) for finding prime numbers.
    :return: A list of integers containing all prime numbers less than or equal to the limit.
    :raises ValueError: If the limit is less than 2.
    """
    if limit < 2:
        raise ValueError("Limit must be greater than or equal to 2.")

    is_prime = [True] * (limit + 1)  # Create a list to track prime status
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Sieve of Eratosthenes algorithm
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Collecting all prime numbers
    primes = [i for i in range(2, limit + 1) if is_prime[i]]

    return primes