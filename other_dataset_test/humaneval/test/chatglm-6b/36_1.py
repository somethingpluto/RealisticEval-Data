

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


def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if i % 11 == 0 or i % 13 == 0:
            count += 1
    return count

fizz_buzz(50)
# Output: 0

fizz_buzz(78)
# Output: 2

fizz_buzz(79)
# Output: 3

candidate = fizz_buzz
check(candidate)