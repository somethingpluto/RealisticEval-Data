

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'
def string_sequence(n: int) -> str:
    sequence =''.join(str(i) for i in range(n + 1))
    return sequence
candidate = string_sequence
check(candidate)