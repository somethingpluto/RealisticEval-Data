

METADATA = {}


def check(candidate):
    assert candidate(50) == 0
    assert candidate(78) == 2
    assert candidate(79) == 3
    assert candidate(100) == 3
    assert candidate(200) == 6
    assert candidate(4000) == 192
    assert candidate(10000) == 639
    assert candidate(100000) == 8026

def fizz_buzz(n: int):
    count = 0
    for i in range(n):
        if (i % 11 == 0 or i % 13 == 0) and str(i).count('7') > 0:
            count += 1
    return count
candidate = fizz_buzz
check(candidate)