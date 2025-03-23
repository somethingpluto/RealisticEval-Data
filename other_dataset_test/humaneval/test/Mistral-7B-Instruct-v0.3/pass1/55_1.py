

METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144

def fib(n: int):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
candidate = fib
check(candidate)