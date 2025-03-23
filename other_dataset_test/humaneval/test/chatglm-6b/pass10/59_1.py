

METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


def largest_prime_factor(n: int) -> int:
    if n <= 1:
        return n
    else:
        primes = [p for p in range(2, int(n ** 0.5) + 1) if 2 <= p <= n]
        return largest_prime_factor(primes[-1])

candidate = largest_prime_factor
check(candidate)