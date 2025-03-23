

METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


def fib4(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

candidate = fib4
check(candidate)