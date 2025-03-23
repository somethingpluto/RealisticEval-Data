

METADATA = {}


def check(candidate):
    assert candidate(2) == 1
    assert candidate(1) == 0
    assert candidate(5) == 4
    assert candidate(8) == 24
    assert candidate(10) == 81
    assert candidate(12) == 274
    assert candidate(14) == 927

def fibfib(n: int):
    fib_fib = [0] * (n + 1)
    fib_fib[0], fib_fib[1], fib_fib[2] = 0, 0, 1

    for i in range(3, n + 1):
        fib_fib[i] = fib_fib[i - 1] + fib_fib[i - 2] + fib_fib[i - 3]

    return fib_fib[n]
candidate = fibfib
check(candidate)