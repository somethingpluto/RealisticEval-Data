

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('x') == 'x'
    assert candidate('xyz') == 'xyzyx'
    assert candidate('xyx') == 'xyx'
    assert candidate('jerry') == 'jerryrrej'

# Test the is_palindrome function
>>> is_palindrome('cat')
True

# Test the make_palindrome function
>>> make_palindrome('')
''

# Test the make_palindrome function with a string
>>> make_palindrome('cat')
'catac'

# Test the make_palindrome function with a string that is not a palindrome
>>> make_palindrome('cat')
False

candidate = make_palindrome
check(candidate)