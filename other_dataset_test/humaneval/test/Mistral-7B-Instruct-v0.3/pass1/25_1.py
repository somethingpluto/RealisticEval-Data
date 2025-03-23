

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(2) == [2]
    assert candidate(4) == [2, 2]
    assert candidate(8) == [2, 2, 2]
    assert candidate(3 * 19) == [3, 19]
    assert candidate(3 * 19 * 3 * 19) == [3, 3, 19, 19]
    assert candidate(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19]
    assert candidate(3 * 19 * 19 * 19) == [3, 19, 19, 19]
    assert candidate(3 * 2 * 3) == [2, 3, 3]
from typing import List

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorize_helper(n: int, primes: List[int]) -> List[int]:
    factors = []
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            factors.append(prime)
            n //= prime
    if n > 1:
        factors.append(n)
    return factors

def factorize(n: int) -> List[int]:
    primes = []
    sieve = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return factorize_helper(n, primes)
candidate = factorize
check(candidate)