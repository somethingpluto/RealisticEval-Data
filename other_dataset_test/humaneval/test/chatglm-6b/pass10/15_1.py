

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'
scss
>>> string_sequence(0)
'0'
>>> string_sequence(5)
'0 1 2 3 4 5'

candidate = string_sequence
check(candidate)