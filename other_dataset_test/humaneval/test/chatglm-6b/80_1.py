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
    if len(s) <= 1:
        return False
    
    # Check if the length of the string is at least 3
    if len(s) < 3:
        return False
    
    # Check if every 3 consecutive letters are distinct
    for i in range(len(s) // 3 + 1):
        for j in range(i * 3, len(s) // 3 + 1, 3):
            if s[i] == s[j]:
                return False
    
    return True

candidate = is_happy
check(candidate)