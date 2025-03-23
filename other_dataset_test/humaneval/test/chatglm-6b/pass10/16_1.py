

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('abcde') == 5
    assert candidate('abcde' + 'cade' + 'CADE') == 5
    assert candidate('aaaaAAAAaaaa') == 1
    assert candidate('Jerry jERRY JeRRRY') == 5

count_distinct_characters('xyzXYZ')
python
def count_distinct_characters(string: str) -> int:
    """Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Count the number of distinct characters
    distinct_characters = 0
    for char in string:
        distinct_characters += 1
    # Return the total number of distinct characters
    return distinct_characters

string ='Jerry '
print(count_distinct_characters(string)) # Output: 4

candidate = count_distinct_characters
check(candidate)