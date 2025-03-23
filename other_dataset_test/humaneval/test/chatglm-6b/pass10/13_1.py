

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12

>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5

candidate = greatest_common_divisor
check(candidate)