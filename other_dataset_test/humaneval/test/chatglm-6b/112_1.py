def check(candidate):

    assert candidate("abcde","ae") == ('bcd',False)
    assert candidate("abcdef", "b") == ('acdef',False)
    assert candidate("abcdedcba","ab") == ('cdedc',True)
    assert candidate("dwik","w") == ('dik',False)
    assert candidate("a","a") == ('',True)
    assert candidate("abcdedcba","") == ('abcdedcba',True)
    assert candidate("abcdedcba","v") == ('abcdedcba',True)
    assert candidate("vabba","v") == ('abba',True)
    assert candidate("mamma", "mia") == ("", True)

def reverse_delete(s, c):
    result = s.copy()
    for char in c:
        if char in result:
            result.remove(char)
    return result, True if result.ispalindrome() else False

s = "abcde"
c = "ae"
result = reverse_delete(s, c)
print(result)  # Output: 'bcd'
print(result.ispalindrome())  # Output: False

s = "abcdef"
c = "b"
result = reverse_delete(s, c)
print(result)  # Output: 'acdef'
print(result.ispalindrome())  # Output: False

s = "abcdedcba"
c = "ab"
result = reverse_delete(s, c)
print(result)  # Output: 'cdedc'
print(result.ispalindrome())  # Output: True

candidate = reverse_delete
check(candidate)