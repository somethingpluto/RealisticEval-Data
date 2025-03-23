

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7
def largest_divisor(n: int) -> int:
    for i in range(1, n):
        if n % i == 0:
            return i
    return n - 1
candidate = largest_divisor
check(candidate)