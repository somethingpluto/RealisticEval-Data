

METADATA = {}


def check(candidate):
    assert candidate(3, 5) == 3
    assert candidate(1101, 101) == 2
    assert candidate(0, 101) == 1
    assert candidate(3, 11) == 8
    assert candidate(100, 101) == 1
    assert candidate(30, 5) == 4
    assert candidate(31, 5) == 3

from functools import reduce

def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    if p == 1:
        return 0

    result = 2
    while n > 1:
        if n % 2 == 1:
            result = (result * result) % p
        n = n // 2
        result = (result * result) % p

    return result
candidate = modp
check(candidate)