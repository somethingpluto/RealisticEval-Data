

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['x', 'y', 'z']) == 'xyz'
    assert candidate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenates a list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the concatenation of the input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
candidate = concatenate
check(candidate)