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
    # Create a dictionary to store the characters in s and their counts
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Remove the characters in c from the dictionary and create a new string
    for char in c:
        if char in char_count:
            if char_count[char] > 0:
                char_count[char] -= 1
            else:
                raise ValueError("All characters in c are not present in s")

    # Create the new string
    new_s = ""
    for char, count in char_count.items():
        new_s += char * count

    # Check if the new string is a palindrome
    new_s_reversed = new_s[::-1]
    if new_s == new_s_reversed:
        return (new_s, True)
    else:
        return (new_s, False)
candidate = reverse_delete
check(candidate)