

METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386

def fib4(n: int):
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[0], fib4_sequence[1], fib4_sequence[2], fib4_sequence[3] = 0, 0, 2, 0

    for i in range(4, n + 1):
        fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]

    return fib4_sequence[n]
candidate = fib4
check(candidate)