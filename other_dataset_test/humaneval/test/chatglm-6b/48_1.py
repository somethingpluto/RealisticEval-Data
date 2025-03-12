

METADATA = {}


def check(candidate):
    assert candidate('') == True
    assert candidate('aba') == True
    assert candidate('aaaaa') == True
    assert candidate('zbcd') == False
    assert candidate('xywyx') == True
    assert candidate('xywyz') == False
    assert candidate('xywzx') == False


>>> is_palindrome('')
True

>>> is_palindrome('aba')
True

>>> is_palindrome('aaaaa')
True

>>> is_palindrome('zbcd')
False

candidate = is_palindrome
check(candidate)