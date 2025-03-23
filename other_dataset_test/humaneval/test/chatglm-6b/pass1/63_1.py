

METADATA = {}


def check(candidate):
    assert candidate(2) == 1
    assert candidate(1) == 0
    assert candidate(5) == 4
    assert candidate(8) == 24
    assert candidate(10) == 81
    assert candidate(12) == 274
    assert candidate(14) == 927


def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2)
python
>>> fibfib(5)
4

candidate = fibfib
check(candidate)