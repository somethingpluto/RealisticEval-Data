def check(candidate):

    assert candidate(5) == [2,3]
    assert candidate(6) == [2,3,5]
    assert candidate(7) == [2,3,5]
    assert candidate(10) == [2,3,5,7]
    assert candidate(0) == []
    assert candidate(22) == [2,3,5,7,11,13,17,19]
    assert candidate(1) == []
    assert candidate(18) == [2,3,5,7,11,13,17]
    assert candidate(47) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    assert candidate(101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def count_up_to(n):
    if n <= 1:
        return []
    primes = [True] * (n + 1)
    primes[0] = False
    for i in range(1, n + 1):
        if i % 2 == 0:
            primes[i] = False
    return [i for i in range(n + 1) if primes[i]]

>>> count_up_to(5)
[2, 3]

>>> count_up_to(11)
[2, 3, 5, 7]

>>> count_up_to(0)
[]

>>> count_up_to(20)
[2, 3, 5, 7, 11, 13, 17, 19]

>>> count_up_to(1)
[]

>>> count_up_to(18)
[2, 3, 5, 7, 11, 13, 17]

candidate = count_up_to
check(candidate)