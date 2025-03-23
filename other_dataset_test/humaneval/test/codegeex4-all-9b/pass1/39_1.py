

METADATA = {}


def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89
    assert candidate(6) == 233
    assert candidate(7) == 1597
    assert candidate(8) == 28657
    assert candidate(9) == 514229
    assert candidate(10) == 433494437

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(a):
            count += 1
            if count == n:
                return a
candidate = prime_fib
check(candidate)