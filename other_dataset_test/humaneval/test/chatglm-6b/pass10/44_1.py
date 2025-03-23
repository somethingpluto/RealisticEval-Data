

METADATA = {}


def check(candidate):
    assert candidate(8, 3) == "22"
    assert candidate(9, 3) == "100"
    assert candidate(234, 2) == "11101010"
    assert candidate(16, 2) == "10000"
    assert candidate(8, 2) == "1000"
    assert candidate(7, 2) == "111"
    for x in range(2, 8):
        assert candidate(x, x + 1) == str(x)


def change_base(x: int, base: int) -> str:
    """Change a number x to a base b.
    return the string representation of x after conversion to base b.
    base numbers are less than 10.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 10:
        return f"{x}B"
    elif base == 10:
        return str(x)
    else:
        return f"{base}x{x}B"

>>> change_base(8, 3)
'22'
>>> change_base(8, 2)
'1000'
>>> change_base(7, 2)
'111'

candidate = change_base
check(candidate)