

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9

def strlen(string: str) -> int:
python
    """ Return length of given string
    
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
python
    >>> len('')
    0
    >>> len('abc')
    3

candidate = strlen
check(candidate)