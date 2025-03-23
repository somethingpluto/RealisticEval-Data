

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
def make_palindrome(string: str) -> str:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def find_longest_palindrome(string: str) -> str:
        max_length = len(string)
        max_palindrome = string
        for i in range(1, max_length):
            substring = string[:i] + string[i:][::-1]
            if is_palindrome(substring) and len(substring) > max_length:
                max_length = len(substring)
                max_palindrome = substring
        return max_palindrome

    longest_palindrome = find_longest_palindrome(string)
    if len(string) == len(longest_palindrome):
        return string
    else:
        return string[:len(longest_palindrome)] + longest_palindrome[::-1] + string[len(longest_palindrome:]][::-1]
candidate = make_palindrome
check(candidate)