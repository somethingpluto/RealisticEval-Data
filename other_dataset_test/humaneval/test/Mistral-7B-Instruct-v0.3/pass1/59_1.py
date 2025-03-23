

METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n: int):
    if n < 2:
        raise ValueError("n must be greater than 1")

    for i in range(2, n + 1):
        if n % i!= 0:
            continue
        if is_prime(i):
            return i
        n //= i

    return n
candidate = largest_prime_factor
check(candidate)