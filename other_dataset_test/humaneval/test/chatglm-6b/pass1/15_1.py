

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'
 
>>> string_sequence(5)
'0 1 2 3 4 5'
 
def string_sequence(numbers: List[int]) -> str:
    """ Return a string containing space-delimited numbers in the order they appear in the list.
    >>> string_sequence([0, 1, 2, 3, 4, 5])
    '0 1 2 3 4 5'
    """
    for num in numbers:
        return f"{num} "
 
>>> string_sequence([0, 1, 2, 3, 4, 5])
'0 1 2 3 4 5'

candidate = string_sequence
check(candidate)