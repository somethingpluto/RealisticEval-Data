def check(candidate):

    # Check some simple cases
    assert candidate("AsDf") == "aSdF"
    assert candidate("1234") == "4321"
    assert candidate("ab") == "AB"
    assert candidate("#a@C") == "#A@c"
    assert candidate("#AsdfW^45") == "#aSDFw^45"
    assert candidate("#6@2") == "2@6#"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("#$a^D") == "#$A^d"
    assert candidate("#ccc") == "#CCC"

    # Don't remove this line:

def solve(s):
    if len(s) == 0:
        return s
    
    for i in range(len(s)):
        if s[i] =='':
            s[i] =''.lower()
            s[i] =''.upper()
        else:
            s[i] = s[i].lower()
            s[i] = s[i].upper()
    
    return s.lower() +'' + s.upper()

s = "ab"
print(solve(s))  # Output: AB

s = "#a@C"
print(solve(s))  # Output: "#A@c"

candidate = solve
check(candidate)