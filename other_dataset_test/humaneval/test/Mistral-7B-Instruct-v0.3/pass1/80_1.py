def check(candidate):

    # Check some simple cases
    assert candidate("a") == False , "a"
    assert candidate("aa") == False , "aa"
    assert candidate("abcd") == True , "abcd"
    assert candidate("aabb") == False , "aabb"
    assert candidate("adb") == True , "adb"
    assert candidate("xyy") == False , "xyy"
    assert candidate("iopaxpoi") == True , "iopaxpoi"
    assert candidate("iopaxioi") == False , "iopaxioi"
def is_happy(s):
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i:i+3] == s[i+1:i+4] == s[i+2:i+5]:
            return False

    return True
candidate = is_happy
check(candidate)