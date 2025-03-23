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
    
    result = s
    for i in range(len(s)):
        if s[i] =='' or s[i] == '.':
            result = result.lower().upper() + s[i] + result
        else:
            result = s[i].lower() + s[i].upper()
    
    return result

candidate = solve
check(candidate)