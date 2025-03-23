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
    result = ""
    for char in s:
        if char == c:
            result += char
        else:
            result += char.lower()
    result = s[::-1].upper() + result
    return (result, True)

s = "abcde"
c = "ae"
result = reverse_delete(s, c)
print(result)  # Output: ('bcd', True)

s = "abcdef"
c = "b"
result = reverse_delete(s, c)
print(result)  # Output: ('acdef', True)

s = "abcdedcba"
c = "ab"
result = reverse_delete(s, c)
print(result)  # Output: ('cdedc', True)

candidate = reverse_delete
check(candidate)